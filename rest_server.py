from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from new_listings_scraper import store_new_listing

hostName = "localhost"
serverPort = 8080


class RestServer(BaseHTTPRequestHandler):
    def do_GET(self):

        segments = self.path.split('/')
        if len(segments) == 3:
            apikey = segments[1]
            token = segments[2]


            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            if apikey == "test123":
                self.wfile.write(bytes("ok", "utf-8"))
                store_new_listing(token.upper())
            else:
                self.wfile.write(bytes("authentication failed", "utf-8"))
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()


def start_server():
    webServer = HTTPServer((hostName, serverPort), RestServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    webServer.serve_forever()