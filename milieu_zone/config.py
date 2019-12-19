import os


def get_sentry_dsn():
    return os.getenv('SENTRY_DSN', None)


def get_tma_certificate():
    tma_cert_location = os.getenv('TMA_CERTIFICATE')
    with open(tma_cert_location) as f:
        return f.read()


def get_mijn_ams_cert():
    cert_location = os.getenv("MIJN_DATA_CLIENT_CERT")
    with open(cert_location) as f:
        return f.read()


def get_cleopatra_host():
    return os.getenv('CLEOPATRA_HOST')


def get_cleopatra_pub():
    cert = os.getenv("CLEOPATRA_PUB")
    return cert
