
import sentry_sdk
from flask import Flask, request
from sentry_sdk.integrations.flask import FlaskIntegration
from tma_saml import get_digi_d_bsn

from milieu_zone.api.milieu_zone.cleopatra_connection import CleopatraConnection
from milieu_zone.config import get_sentry_dsn, get_tma_certificate, get_cleopatra_host, get_mijn_ams_cert_path, \
    get_cleopatra_pub, get_mijn_ams_key_path, get_cleopatra_pub_path

app = Flask(__name__)

if get_sentry_dsn():  # pragma: no cover
    sentry_sdk.init(
        dsn=get_sentry_dsn(),
        integrations=[FlaskIntegration()],
        with_locals=False
    )


def get_bsn_from_request(request):
    """
    Get the BSN based on a request, expecting a SAML token in the headers
    """
    # Load the TMA certificate
    tma_certificate = get_tma_certificate()

    # Decode the BSN from the request with the TMA certificate
    bsn = get_digi_d_bsn(request, tma_certificate)
    return bsn


@app.route('/milieu/get', methods=['GET'])
def get_milieu_zone():
    connection = CleopatraConnection(
        get_cleopatra_host(),
        get_mijn_ams_cert_path(),
        get_mijn_ams_key_path(),
        get_cleopatra_pub().encode(),
        get_cleopatra_pub_path()
    )
    try:
        bsn = get_bsn_from_request(request)
    except Exception as e:
        return str(e), 400

    data = connection.get_stuff(bsn)

    return {
        'status': 'OK',
        'data': data,
    }


@app.route('/status/health')
def health_check():
    return 'OK'


if __name__ == '__main__':  # pragma: no cover
    app.run()
