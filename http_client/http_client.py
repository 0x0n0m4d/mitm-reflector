class HTTPData:
    def __init__(self, method, url, params, headers, data) -> None:
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers
        self.data = data


class HTTPResponse:
    def __init__(self, status, headers, body) -> None:
        self.status = status
        self.headers = headers
        self.body = body


class Reflections:
    def __init__(self, url, params, data) -> None:
        self.url = url
        self.params = params
        self.data = data


class HTTPClient:
    import requests

    def __init__(self, method, url, params, headers, data) -> None:
        self.req = HTTPData(
            method,
            url,
            params,
            headers,
            data
        )
        self.resp = None

    def get(self) -> None:
        resp = self.requests.get(self.req.url, params=self.req.params,
                                 headers=self.req.headers, timeout=30)
        self.resp = HTTPResponse(
            resp.status_code,
            resp.headers,
            resp.content
        )

    def post(self) -> None:
        resp = self.requests.post(self.req.url, headers=self.req.headers,
                                  params=self.req.params, data=self.req.data,
                                  timeout=30)
        self.resp = HTTPResponse(
            resp.status_code,
            resp.headers,
            resp.content
        )

    def searchReflections(self) -> Reflections:
        # @todo: this will change the values of all the query and the data one by one
        # @todo: then this needs to save the results on this Reflections class
        return 0
