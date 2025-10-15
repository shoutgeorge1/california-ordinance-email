#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Server running at http://localhost:{PORT}")
    print("📧 Email template: http://localhost:8000/webinar-email.html")
    print("🏠 Landing page: http://localhost:8000/")
    webbrowser.open(f'http://localhost:{PORT}')
    httpd.serve_forever()
