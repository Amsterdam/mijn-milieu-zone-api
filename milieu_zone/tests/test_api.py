import os.path
from unittest.mock import patch

from jwcrypto import jwk
from jwcrypto.common import json_decode
from tma_saml import FlaskServerTMATestCase
from tma_saml.for_tests.cert_and_key import server_crt

from milieu_zone.server import app
from milieu_zone.tests.mocks import RequestsMock


# prepare for mocks
FIXTURE_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')
FIXTURE_MIJN_AMS_CERT_PATH = os.path.join(FIXTURE_PATH, 'mijn_ams.crt')
FIXTURE_MIJN_AMS_KEY_PATH = os.path.join(FIXTURE_PATH, 'mijn_ams.pem')
FIXTURE_CLEOPATRA_CERT_PATH = os.path.join(FIXTURE_PATH, 'cleopatra.crt')

with open(FIXTURE_CLEOPATRA_CERT_PATH) as f:
    FIXTURE_CLEOPATRA_CERT = f.read()


# Mock all the config
@patch("milieu_zone.server.get_tma_certificate", lambda: server_crt)
@patch("milieu_zone.server.get_cleopatra_url", lambda: "http://localhost")
@patch("milieu_zone.server.get_mijn_ams_cert_path", lambda: FIXTURE_MIJN_AMS_CERT_PATH)
@patch("milieu_zone.server.get_mijn_ams_key_path", lambda: FIXTURE_MIJN_AMS_KEY_PATH)
@patch("milieu_zone.server.get_cleopatra_pub_path", lambda: FIXTURE_CLEOPATRA_CERT_PATH)
@patch("milieu_zone.server.get_cleopatra_pub", lambda: FIXTURE_CLEOPATRA_CERT)
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

        response = self.client.get("/milieu/get", headers=SAML_HEADERS)
        self.assertTrue(response)
