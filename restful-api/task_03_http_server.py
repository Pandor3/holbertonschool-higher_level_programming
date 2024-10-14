#!/usr/bin/python3
"""
This module will be used in order to develop
a simple API
"""

import json
import http.server


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Class which will define how the API works
    """


    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                    "name": "John",
                    "age": "30",
                    "city": "New York"
                    }
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                    }
            json_bytes = json.dumps(info_data).encode("utf-8")
            self.wfile.write(json_bytes)
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found")


PORT = 8000

with http.server.HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
