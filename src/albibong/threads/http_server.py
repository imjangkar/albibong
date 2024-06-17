import http.server
import os
import socketserver
import threading
from urllib.parse import urlparse

from albibong.classes.logger import Logger

logger = Logger(__name__, stdout=True, log_to_file=False)
DIRECTORY = os.path.join(os.path.dirname(__file__), "../gui_dist")
INDEXFILE = "/index.html"


class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, directory=DIRECTORY)

    def log_message(self, format, *args):
        # logger.info(format % args)
        pass

    def do_GET(self):
        # Parse query data to find out what was requested
        parsedParams = urlparse(self.path)

        # See if the file requested exists
        if os.access(DIRECTORY + parsedParams.path, os.R_OK):
            # File exists, serve it up
            http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            # send index.html, but don't redirect
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open(DIRECTORY + INDEXFILE, "rb") as fin:
                self.copyfile(fin, self.wfile)


class HttpServerThread(threading.Thread):
    def __init__(self, name, port):
        super().__init__()
        self.name = name
        self.port = port

    def run(self):
        # Create an object of the above class
        handler_object = HttpRequestHandler

        self.http_server = socketserver.TCPServer(("", self.port), handler_object)
        self.http_server.allow_reuse_address = True

        # Star the server
        server_thread = threading.Thread(target=self.http_server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        logger.info(f"Thread {self.name} started at port {self.port}")

    def stop(self):
        self.http_server.shutdown()
        logger.info(f"Thread {self.name} stopped")
