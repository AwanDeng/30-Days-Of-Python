# Day 28 - Simple web server routing setup

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleRouterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Basic route matching
        if self.path == "/":
            message = "<h1>Welcome to Home Page</h1>"
        elif self.path == "/about":
            message = "<h1>About Me Page</h1>"
        else:
            message = "<h1>404 Page Not Found</h1>"

        self.wfile.write(message.encode("utf-8"))

print("Simple Route Handler defined for web routes '/' and '/about'")