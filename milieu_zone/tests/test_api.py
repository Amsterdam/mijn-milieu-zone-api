from unittest.mock import patch

from jwcrypto import jwk
from jwcrypto.common import json_decode
from tma_saml import FlaskServerTMATestCase

from milieu_zone.server import app
from milieu_zone.tests.mocks import RequestsMock


@patch('milieu_zone.api.milieu_zone.cleopatra_connection.requests', RequestsMock)
class ApiTest(FlaskServerTMATestCase):
    TEST_BSN = "111222333"

    def setUp(self) -> None:
        # Create new temporary keys
        self.public_key = jwk.JWK()
        self.private_key = jwk.JWK.generate(kty='RSA', size=2048)
        self.public_key.import_key(**json_decode(self.private_key.export_public()))

        self.client = self.get_tma_test_app(app)

    def test_get(self):
        SAML_HEADERS = self.add_digi_d_headers(self.TEST_BSN)

        response = self.client.get("/decosjoin/getvergunningen", headers=SAML_HEADERS)
        self.assertTrue(response)
