class ResponseMock:
    def content(self):
        return '{}'

    def json(self):
        return {}


class RequestsMock:
    def post(self, *args, **kwargs):
        print("post", args, kwargs)
        return ResponseMock()
