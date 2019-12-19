import os


def _load_file_from_env(env_var):
    location = os.getenv(env_var)
    with open(location) as f:
        return f.read()


def get_sentry_dsn():
    return os.getenv('SENTRY_DSN', None)


def get_tma_certificate():
    return _load_file_from_env("TMA_CERTIFICATE")


def get_mijn_ams_cert_path():
    return os.getenv("MIJN_DATA_CLIENT_CERT")


def get_mijn_ams_key_path():
    return os.getenv("MIJN_DATA_CLIENT_KEY")


def get_cleopatra_host():
    return os.getenv('CLEOPATRA_HOST')


def get_cleopatra_pub():
    cert = os.getenv("CLEOPATRA_PUB")
    return cert
