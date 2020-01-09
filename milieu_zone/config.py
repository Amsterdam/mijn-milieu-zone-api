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


def get_cleopatra_url():
    return os.getenv('CLEOPATRA_URL')


def get_cleopatra_pub_path():
    cert = os.getenv("CLEOPATRA_PUB")
    return cert


def get_cleopatra_pub():
    return _load_file_from_env('CLEOPATRA_PUB')
