import requests
import sys
from mitmproxy import http


def automatedXSSTest() -> bool:
    return True


def request(flow: http.HTTPFlow) -> None:
    # @todo: should match and start doing automated tests on the code
    # @todo: this will get the request and will start making automated tests
    # @todo: then, this will check the response and will start looking to
    # @>>>>> the payload.
    # @todo: if the payload was found, then this will save this on a file
    if flow.request.method == "GET":
        for k, v in flow.request.query.items():
            print(v)
