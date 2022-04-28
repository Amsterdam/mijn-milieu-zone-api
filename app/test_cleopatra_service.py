import os
from unittest import TestCase
from unittest.mock import patch
from app.auth import PROFILE_TYPE_PRIVATE

from app.cleopatra_service import CleopatraConnection

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures")
FIXTURE_MIJN_AMS_CERT_PATH = os.path.join(FIXTURE_PATH, "mijn_ams.crt")
FIXTURE_MIJN_AMS_KEY_PATH = os.path.join(FIXTURE_PATH, "mijn_ams.pem")
FIXTURE_CLEOPATRA_CERT_PATH = os.path.join(FIXTURE_PATH, "cleopatra.crt")


class CleopatraConnectionTest(TestCase):
    @patch("app.cleopatra_service.CleopatraConnection._get_jwe_token")
    @patch("app.cleopatra_service.requests.post")
    def test_get(self, post_request_mock, _get_jwe_token_mock):

        jwe_payload = '{"ciphertext":"5sa-690eqEv6yOassVwqPbHnguz5mDSvL_stEjlUdwU","encrypted_key":"biCP_3E2QBK06T90nP0Gv1NGx_pToxG_hwLmnBTxiwc3e2r0v4kVBDOlV7VAfhXnjWBZ3QY4IPozzLsOeZTQmLIb7H12Z0QUEI9Yc0jE4Wkx9vm8rm9O6Pc7enq8j2Hmx4BpMfmWAh9Os7wmS5dus_4gtz014K04ufc4vQunQDabD-rNJdqdP413fsT1oFUqD1Sb7EHqZSnF7cjx6feZ-OpUI6gy5V4GjFLT6iZ2FIuIEmd4_twV0cMy78YuBF3jfbFN2LhqiqweFoYwq3Bc68mBXnjHaQGlS53yW70FhEhY-OmzKd2WXI6ENz728fz8tVI_RUNuuoz21UZ_CWp9DQ","iv":"R_SmTEPinZq2GJCCudb5Qg","protected":"eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwia2lkIjoialpXTTBKY1RvT1pIQUZEZnJ1bGtoMWVHeC0tdVBpbUk1NlJ5TkZCcHpjbyIsInR5cCI6IkpXRSJ9","tag":"HIH8Ozer502YobfRjXbe61gnVKC4wEmJkNQnSTo0GF0"}'
        _get_jwe_token_mock.return_value = jwe_payload

        con = CleopatraConnection(
            "http://localhost/",
            FIXTURE_MIJN_AMS_CERT_PATH,
            FIXTURE_MIJN_AMS_KEY_PATH,
            FIXTURE_CLEOPATRA_CERT_PATH,
        )
        result = con.get_stuff({"type": PROFILE_TYPE_PRIVATE, "id": "123-bsn"})

        post_request_mock.assert_called_with(
            "http://localhost/",
            verify=False,
            data=jwe_payload,
            cert=(
                FIXTURE_MIJN_AMS_CERT_PATH,
                FIXTURE_MIJN_AMS_KEY_PATH,
            ),
        )

        self.assertEqual(result, {"tips": [], "meldingen": [], "isKnown": False})
