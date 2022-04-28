import logging
import os
import os.path
from datetime import date, time

from flask.json import JSONEncoder

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
FIXTURES_PATH = os.path.join(BASE_PATH, "fixtures")

# Sentry configuration.
SENTRY_DSN = os.getenv("SENTRY_DSN")
SENTRY_ENV = os.getenv("SENTRY_ENVIRONMENT")

# Environment determination
IS_PRODUCTION = SENTRY_ENV == "production"
IS_ACCEPTANCE = SENTRY_ENV == "acceptance"
IS_AP = IS_PRODUCTION or IS_ACCEPTANCE
IS_DEV = os.getenv("FLASK_ENV") == "development" and not IS_AP

# App constants
ENABLE_OPENAPI_VALIDATION = os.getenv("ENABLE_OPENAPI_VALIDATION", not IS_AP)

# Set-up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "ERROR").upper()

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in function %(funcName)s] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=LOG_LEVEL,
)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, time):
            return obj.isoformat(timespec="minutes")
        if isinstance(obj, date):
            return obj.isoformat()

        return JSONEncoder.default(self, obj)


def _load_file_from_env(env_var):
    location = os.getenv(env_var)
    with open(location) as f:
        return f.read()


def get_mijn_ams_cert_path():
    return os.getenv("MIJN_DATA_CLIENT_CERT")


def get_mijn_ams_key_path():
    return os.getenv("MIJN_DATA_CLIENT_KEY")


def get_cleopatra_url():
    return os.getenv("CLEOPATRA_URL")


def get_cleopatra_pub_path():
    cert = os.getenv("CLEOPATRA_PUB")
    return cert


def get_cleopatra_pub():
    return _load_file_from_env("CLEOPATRA_PUB")
