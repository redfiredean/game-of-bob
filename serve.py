import http.server
import socketserver
import os
import sys

port = int(os.environ.get("PORT", 8080))
directory = "/Users/deanfanton/Documents/Claude/game-of-bob"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)
    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving on port {port}", flush=True)
    httpd.serve_forever()
