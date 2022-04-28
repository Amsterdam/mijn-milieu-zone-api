import os.path
from unittest.mock import patch

from app.auth import PROFILE_TYPE_COMMERCIAL, FlaskServerTestCase
from app.fixtures.get_response import get_all_expected, get_all_source

from app.server import app


# prepare for mocks
FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures")
FIXTURE_MIJN_AMS_CERT_PATH = os.path.join(FIXTURE_PATH, "mijn_ams.crt")
FIXTURE_MIJN_AMS_KEY_PATH = os.path.join(FIXTURE_PATH, "mijn_ams.pem")
FIXTURE_CLEOPATRA_CERT_PATH = os.path.join(FIXTURE_PATH, "cleopatra.crt")

with open(FIXTURE_CLEOPATRA_CERT_PATH) as f:
    FIXTURE_CLEOPATRA_CERT = f.read()


class HealthTest(FlaskServerTestCase):
    app = app

    def test_status(self):
        response = self.client.get("/status/health")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "OK")
        self.assertEqual(data["content"], "OK")


# Mock all the config
@patch("app.server.get_cleopatra_url", lambda: "http://localhost")
@patch("app.server.get_mijn_ams_cert_path", lambda: FIXTURE_MIJN_AMS_CERT_PATH)
@patch("app.server.get_mijn_ams_key_path", lambda: FIXTURE_MIJN_AMS_KEY_PATH)
@patch("app.server.get_cleopatra_pub_path", lambda: FIXTURE_CLEOPATRA_CERT_PATH)
class BSNApiTest(FlaskServerTestCase):
    app = app

    @patch("app.cleopatra_service.CleopatraConnection.get_data")
    def test_invalid(self, get_data_mock):
        get_data_mock.return_value = get_all_expected()
        response = self.client.get("/milieu/get")

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["status"], "ERROR")
        self.assertEqual(response.json["message"], "Auth error occurred")

    @patch("app.cleopatra_service.CleopatraConnection.get_data")
    def test_get(self, get_data_mock):
        get_data_mock.return_value = get_all_source()
        response = self.get_secure("/milieu/get")

        self.assertEqual(response.json, get_all_expected())


# Mock all the config
@patch("app.server.get_cleopatra_url", lambda: "http://localhost")
@patch("app.server.get_mijn_ams_cert_path", lambda: FIXTURE_MIJN_AMS_CERT_PATH)
@patch("app.server.get_mijn_ams_key_path", lambda: FIXTURE_MIJN_AMS_KEY_PATH)
@patch("app.server.get_cleopatra_pub_path", lambda: FIXTURE_CLEOPATRA_CERT_PATH)
class KVKApiTest(FlaskServerTestCase):
    app = app

    @patch("app.cleopatra_service.CleopatraConnection.get_data")
    def test_get(self, get_data_mock):
        get_data_mock.return_value = get_all_source()
        response = self.get_secure("/milieu/get", profile_type=PROFILE_TYPE_COMMERCIAL)

        self.assertEqual(response.json, get_all_expected())
