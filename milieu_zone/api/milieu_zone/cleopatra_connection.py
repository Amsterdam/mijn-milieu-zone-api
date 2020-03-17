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

    def _get_jwe_token(self, request_id_obj):
        """ Return the encoded JWE token containing the BSN. """
        # Inspired by https://jwcrypto.readthedocs.io/en/latest/jwe.html#asymmetric-keys
        payload = json.dumps(request_id_obj)

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

    def get_data(self, request_id_obj):
        jwe_token = self._get_jwe_token(request_id_obj)
        response = requests.post(
            self.cleopatra_api_url,
            # verify=self.cleopatra_pub_path,  # TODO: needs to be added to the "global store" instead of being specific
            verify=False,
            data=jwe_token,
            cert=(self.client_public_path, self.client_priv_path)
        )
        return response.json()

    def _format_data(self, data_item):
        i = data_item
        return {
            "id": 'milieu-' + i["categorie"],  # FIXME: these are not unique enough
            "priority": i["prioriteit"],
            "datePublished": i["datum"],
            "title": i["titel"],
            "description": i["omschrijving"],
            "link": {
                "title": i["urlNaam"],
                "to": i["url"],
            }
        }

    def transform(self, data):
        res = {
            "tips": [],
            "meldingen": [],
            "isKnown": False
        }

        for i in data:
            if i['categorie'] == "F2":
                res['isKnown'] = True

            elif i['categorie'] == 'F3':
                melding = self._format_data(i)
                res['meldingen'].append(melding)

            elif i['categorie'] == 'M1':
                melding = self._format_data(i)
                res['meldingen'].append(melding)

            # M2 comes from the tips-api. content tip
            # elif i['categorie'] == 'M2':
            #     tip = self._format_data(i)
            #     res['tips'].append(tip)

        return res

    def get_stuff(self, request_id_obj):
        data = self.get_data(request_id_obj)
        data = self.transform(data)
        return data
