import sys

import milieu_zone
from milieu_zone.api.milieu_zone.cleopatra_connection import CleopatraConnection
from milieu_zone.config import get_mijn_ams_cert_path, get_mijn_ams_key_path, get_cleopatra_pub_path, get_cleopatra_url

bsn = sys.argv[1]


milieu_zone.api.milieu_zone.cleopatra_connection.log_raw = True


connection = CleopatraConnection(
    get_cleopatra_url(),
    get_mijn_ams_cert_path(),
    get_mijn_ams_key_path(),
    get_cleopatra_pub_path()
)

resposne = connection.get_stuff(bsn)
