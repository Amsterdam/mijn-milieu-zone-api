import json

import requests
from jwcrypto import jwe, jwk

from app.auth import PROFILE_TYPE_COMMERCIAL


class CleopatraConnection:
    def __init__(
        self,
        cleopatra_api_url,
        client_public_cert_path,
        client_priv_cert_path,
        cleopatra_pub_path,
    ):
        self.cleopatra_api_url = cleopatra_api_url
        self.client_public_path = client_public_cert_path
        self.client_priv_path = client_priv_cert_path

        self.cleopatra_pub_path = cleopatra_pub_path

        with open(self.cleopatra_pub_path, "rb") as fp:
            self.cleopatra_pub = fp.read()

    def _get_jwe_token(self, request_id_obj):
        """Return the encoded JWE token containing the BSN."""
        # Inspired by https://jwcrypto.readthedocs.io/en/latest/jwe.html#asymmetric-keys
        payload = json.dumps(request_id_obj)

        public_key = jwk.JWK.from_pem(self.cleopatra_pub)
        protected_header = {
            "alg": "RSA-OAEP-256",
            "enc": "A256CBC-HS512",
            "typ": "JWE",
            "kid": public_key.thumbprint(),
        }
        jwetoken = jwe.JWE(
            payload.encode("utf-8"), recipient=public_key, protected=protected_header
        )

        enc = jwetoken.serialize()
        return enc

    def get_data(self, user):
        if user["type"] == PROFILE_TYPE_COMMERCIAL:
            payload = {"kvk": user["id"]}
        else:
            payload = {"bsn": user["id"]}

        jwe_token = self._get_jwe_token(payload)
        url = self.cleopatra_api_url

        response = requests.post(
            url,
            verify=False,
            data=jwe_token,
            cert=(self.client_public_path, self.client_priv_path),
        )

        response.raise_for_status()

        return response.json()

    def _format_data(self, data_item):
        return {
            "id": "milieu-"
            + data_item["categorie"],  # FIXME: these are not unique enough
            "priority": data_item["prioriteit"],
            "datePublished": data_item["datum"],
            "title": data_item["titel"],
            "description": data_item["omschrijving"],
            "link": {
                "title": data_item["urlNaam"],
                "to": data_item["url"],
            },
        }

    def transform(self, data):
        res = {"tips": [], "meldingen": [], "isKnown": False}

        for item in data:
            if item["categorie"] == "F2":
                res["isKnown"] = True

            elif item["categorie"] == "F3":
                melding = self._format_data(item)
                res["meldingen"].append(melding)

            elif item["categorie"] == "M1":
                melding = self._format_data(item)
                res["meldingen"].append(melding)

        return res

    def get_stuff(self, user):
        data = self.get_data(user)
        data = self.transform(data)
        return data
