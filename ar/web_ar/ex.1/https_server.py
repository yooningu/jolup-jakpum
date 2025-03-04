import http.server
import ssl

httpd = http.server.HTTPServer(('0.0.0.0', 8000), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='server.key', certfile='server.crt', server_side=True)
print("Server started on https://0.0.0.0:8000")
httpd.serve_forever()
