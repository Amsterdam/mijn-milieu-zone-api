import requests
import json

from jwcrypto import jwe, jwk


class CleopatraConnection:

    def __init__(self, cleopatra_api_url, client_public_cert_path, client_priv_cert_path, cleopatra_pub_path):
        self.cleopatra_api_url = cleopatra_api_url
        self.client_public_path = client_public_cert_path
        self.client_priv_path = client_priv_cert_path

        self.cleopatra_pub_path = cleopatra_pub_path

        with open(self.cleopatra_pub_path, 'rb') as fp:
            self.cleopatra_pub = fp.read()

    def _get_jwe_token(self, bsn):
        """ Return the encoded JWE token containing the BSN. """
        # Inspired by https://jwcrypto.readthedocs.io/en/latest/jwe.html#asymmetric-keys
        payload = json.dumps({'bsn': bsn})

        public_key = jwk.JWK.from_pem(self.cleopatra_pub)
        protected_header = {
            "alg": "RSA-OAEP-256",
            "enc": "A256CBC-HS512",
            "typ": "JWE",
            "kid": public_key.thumbprint(),
        }
        jwetoken = jwe.JWE(payload.encode('utf-8'),
                           recipient=public_key,
                           protected=protected_header)

        enc = jwetoken.serialize()
        return enc

    def get_stuff(self, bsn):
        jwe_token = self._get_jwe_token(bsn)
        res = requests.post(
            self.cleopatra_api_url,
            # verify=self.cleopatra_pub_path,  # TODO: needs to be added to the "global store" instead of being specific
            verify=False,
            data=jwe_token,
            cert=(self.client_public_path, self.client_priv_path)
        )
        # print(res.content)
        return res.json()
