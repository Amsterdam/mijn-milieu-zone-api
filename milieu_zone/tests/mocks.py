import json
import os

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')
FIXTURE_ALL_PATH = os.path.join(FIXTURE_PATH, 'all.json')


def get_fixture_all():
    with open(FIXTURE_ALL_PATH) as fp:
        return fp.read()


class ResponseMock:
    def content(self):
        return '{}'

    def json(self):
        return json.loads(get_fixture_all())


class RequestsMock:
    def post(self, *args, **kwargs):
        print("\n\n>>> ---------- POST\n", args, kwargs)
        return ResponseMock()
