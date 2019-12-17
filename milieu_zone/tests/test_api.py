from unittest import TestCase
from unittest.mock import patch

from jwcrypto import jwk
from jwcrypto.common import json_decode

from milieu_zone.api.milieu_zone.cleopatra_connection import CleopatraConnection


class ResponseMock:
    def content(self):
        return ''


class RequestsMock:
    def post(self, *args, **kwargs):
        print("post", args, kwargs)
        return ResponseMock()


@patch('milieu_zone.api.milieu_zone.cleopatra_connection.requests', RequestsMock)
class CleopatraConnectionTest(TestCase):
    def setUp(self) -> None:

        # Create new temporary keys
        self.public_key = jwk.JWK()
        self.private_key = jwk.JWK.generate(kty='RSA', size=2048)
        self.public_key.import_key(**json_decode(self.private_key.export_public()))

    def test_get(self):
        con = CleopatraConnection("http://localhost/", self.public_key.export_to_pem())
        result = con.get_stuff("111222333")
        self.assertFalse(result)
