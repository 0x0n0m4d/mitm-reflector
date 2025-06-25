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


class HTTPClient:
    import requests

    def __init__(self, method, url, params, headers, data) -> None:
        self.data = HTTPData(
            method,
            url,
            params,
            headers,
            data
        )

    def get(self) -> HTTPResponse:
        resp = self.requests.get(self.data.url, params=self.data.params,
                                 headers=self.data.headers, timeout=30)
        return HTTPResponse(
            status=resp.status_code,
            headers=resp.headers,
            body=resp.content
        )

    def post(self) -> HTTPResponse:
        resp = self.requests.post(self.data.url, headers=self.data.headers,
                                  params=self.data.params, data=self.data.data,
                                  timeout=30)
        return HTTPResponse(
            status=resp.status_code,
            headers=resp.headers,
            body=resp.content
        )
