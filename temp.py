from http.server import HTTPServer, BaseHTTPRequestHandler
# HTTPServer is used to start a server
# BaseHTTPRequestHandler is used to manage get and post


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path.encode())


def main():
    PORT = 8000
    # helloHandler is a class name used to work on get and post
    server = HTTPServer(('', PORT), helloHandler)
    print("Server is running on Port %s" % PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()
