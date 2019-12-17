import requests
import json

from jwcrypto import jwe, jwk


class CleopatraConnection:

    def __init__(self, cleopatra_host, client_public_cert):
        self.cleopatra_host = cleopatra_host
        self.client_public = client_public_cert

    def _get_jwe_token(self, bsn):
        """ Return the encoded JWE token containing the BSN. """
        # Inspired by https://jwcrypto.readthedocs.io/en/latest/jwe.html#asymmetric-keys
        payload = json.dumps({'bsn': bsn})

        public_key = jwk.JWK.from_pem(self.client_public)
        protected_header = {
            "alg": "RSA-OAEP-256",
            "enc": "A256CBC-HS512",
            "typ": "JWE",
            "kid": public_key.thumbprint(),
        }
        jwetoken = jwe.JWE(payload.encode('utf-8'),
                           recipient=public_key,
                           protected=protected_header)

        print("jwe token", jwetoken)
        enc = jwetoken.serialize()
        print("serialized jwe token", enc)
        return enc

    def get_stuff(self, bsn):
        # res = requests.post(self.cleopatra_host, verify=get_cleopatra_cert(), data={})
        jwe_token = self._get_jwe_token(bsn)
        res = requests.post(self.cleopatra_host, verify=False, data=jwe_token)
        return res
