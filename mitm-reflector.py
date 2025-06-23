import logging
from mitmproxy import http
from mitmproxy import addonmanager


# @todo: create a http client
# @todo: create the xss tester
class Reflector:
    def __init__(self) -> None:
        self.endpoints = dict()

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
        else:
            if len(flow.request.content) <= 0:
                return


addons = [Reflector()]
