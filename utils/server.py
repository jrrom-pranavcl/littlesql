from .repl import parse

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import time
import traceback

# ==================== CONSTANTS ====================

HOST_NAME = "localhost"
SERVER_PORT = 42069
ENCODING = "UTF-8"
BASE_URL = "client"

# ==================== ROUTES =======================

def get_root(web_server):
    web_server.create_headers()
    web_server.serve_webpage()

def post_query(web_server):
    web_server.create_headers(content_type="application/json")

    try:
        web_server.wfile.write(bytes(parse(str(web_server.body, ENCODING)), ENCODING))
    except Exception:
        web_server.wfile.write(bytes(traceback.format_exc(), ENCODING))

GET_ROUTES = {
    "/": get_root
}

POST_ROUTES = {
    "/query": post_query
}

# ==================== SERVER =======================

class WebServer(BaseHTTPRequestHandler):
    def create_headers(self, resp_status=200, content_type="text/html"):
        self.send_response(resp_status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def serve_webpage(self, url="index.html"):
        with open(f"{BASE_URL}/{url}", "r") as file:
            self.wfile.write(bytes(file.read(), ENCODING))

    def do_GET(self):
        try:
            GET_ROUTES[self.path](self)
        except KeyError:
            self.create_headers(404, "text/html")
            self.wfile.write(b"<h1>404 Not Found</h1><p>Whoops</p>")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        self.body = self.rfile.read(content_length)

        try:
            POST_ROUTES[self.path](self)
        except KeyError:
            self.create_headers(404, "text/html")
            self.wfile.write(b"<h1>404 Not Found</h1><p>Whoops</p>")

class ThreadedWebServer(ThreadingMixIn, HTTPServer):
    pass

# ==================== MAIN LOOP =======================

def server() -> None:
    web_server = ThreadedWebServer((HOST_NAME, SERVER_PORT), WebServer)
    print(f":) Server started on http://{HOST_NAME}:{SERVER_PORT}\t")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")

# ======================================================

