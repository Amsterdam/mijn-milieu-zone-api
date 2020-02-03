class ResponseMock:
    def content(self):
        return '{}'

    def json(self):
        return {}


class RequestsMock:
    def post(self, *args, **kwargs):
        print("\n\n>>> ---------- POST\n", args, kwargs)
        return ResponseMock()
