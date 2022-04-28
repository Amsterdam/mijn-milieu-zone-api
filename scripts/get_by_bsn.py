from pprint import pprint
import sys

from app.cleopatra_service import CleopatraConnection
from app.config import (
    get_mijn_ams_cert_path,
    get_mijn_ams_key_path,
    get_cleopatra_pub_path,
    get_cleopatra_url,
)

bsn = sys.argv[1]

connection = CleopatraConnection(
    get_cleopatra_url(),
    get_mijn_ams_cert_path(),
    get_mijn_ams_key_path(),
    get_cleopatra_pub_path(),
)

response = connection.get_stuff(bsn)

pprint(response)
