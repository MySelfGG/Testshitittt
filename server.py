import http.server
import socketserver

PORT = 8000  # You can change this to any port you want

Handler = http.server.SimpleHTTPRequestHandler

while True:
    with socketserver.TCPServer(("192.168.228.51", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
    x = Input("stop für stop : ")
    if x == "stop":
        break
