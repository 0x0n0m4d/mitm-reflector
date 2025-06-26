import logging
from mitmproxy import http
from mitmproxy import addonmanager
from http_client import HTTPClient


# @todo: create the xss tester
class Reflector:
    def __init__(self) -> None:
        self.endpoints = []

    def newEndpointItem(self, endpoint: str, status: int,
                        method: str, params: list, data: list,
                        payload: str) -> None:
        self.endpoints.append(dict(
            endpoint=endpoint,
            status=status,
            method=method,
            params=params,
            data=data,
            payload=payload
        ))

    def load(self, loader: addonmanager.Loader) -> None:
        loader.add_option(
            name="xss_mode",
            typespec=str,
            default="passive",
            help="Define the mode of the reflector: `-s mitm-reflector.py --set xss_mode='aggressive'`"
        )
        logging.info("mitm-reflector.py loaded")

    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.method == "GET":
            if len(flow.request.query.items()) <= 0:
                return

            client = HTTPClient(
                flow.request.method,
                flow.request.url,
                flow.request.query.items(),
                flow.request.headers,
                dict()
            )
            reflection = client.searchReflections()
            if reflection is not None:
                self.endpoints.append(client.searchReflections())

            logging.warn(f"find {len(self.endpoints.params)} reflections")
        else:
            if len(flow.request.content) <= 0 and \
                    len(flow.request.query.items() <= 0):
                return

            client = HTTPClient(
                flow.request.method,
                flow.request.url,
                flow.request.query.items(),
                flow.request.headers,
                flow.request.content
            )
            reflection = client.searchReflections()
            if reflection is not None:
                self.endpoints.append(client.searchReflections())

            logging.warn(f"find {len(self.endpoints.params)} reflections")
    # @todo: i need a command to replay this logs


addons = [Reflector()]
