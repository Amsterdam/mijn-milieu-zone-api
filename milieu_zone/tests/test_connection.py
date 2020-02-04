import os
from unittest import TestCase
from unittest.mock import patch

from jwcrypto import jwk
from jwcrypto.common import json_decode

from milieu_zone.api.milieu_zone.cleopatra_connection import CleopatraConnection
from milieu_zone.tests.mocks import RequestsMock

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')
FIXTURE_MIJN_AMS_CERT_PATH = os.path.join(FIXTURE_PATH, 'mijn_ams.crt')
FIXTURE_MIJN_AMS_KEY_PATH = os.path.join(FIXTURE_PATH, 'mijn_ams.pem')
FIXTURE_CLEOPATRA_CERT_PATH = os.path.join(FIXTURE_PATH, 'cleopatra.crt')


@patch('milieu_zone.api.milieu_zone.cleopatra_connection.requests', RequestsMock)
class CleopatraConnectionTest(TestCase):
    def setUp(self) -> None:

        # Create new temporary keys
        self.public_key = jwk.JWK()
        self.private_key = jwk.JWK.generate(kty='RSA', size=2048)
        self.public_key.import_key(**json_decode(self.private_key.export_public()))

        # Cleopatra
        self.cleo_pub = jwk.JWK()
        cleo_priv = jwk.JWK.generate(kty='RSA', size=2048)
        self.cleo_pub.import_key(**json_decode(cleo_priv.export_public()))

    def test_get(self):
        con = CleopatraConnection(
            "http://localhost/",
            FIXTURE_MIJN_AMS_CERT_PATH,
            FIXTURE_MIJN_AMS_KEY_PATH,
            FIXTURE_CLEOPATRA_CERT_PATH,
        )
        result = con.get_stuff("111222333")
        self.assertEqual(result, {})
