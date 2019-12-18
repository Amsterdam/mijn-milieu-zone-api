class ResponseMock:
    def content(self):
        return ''


class RequestsMock:
    def post(self, *args, **kwargs):
        print("post", args, kwargs)
        return ResponseMock()
