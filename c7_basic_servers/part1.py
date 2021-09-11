from http.server import HTTPServer,BaseHTTPRequestHandler

with open('index.html')as file:
    html=file.read()

phonebook={'key1':1}


class WebPhonebook(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        content=''
        for name,number in phonebook.items():
            content+=f"""  
    <tr>
        <th align="left">{name}</td>
        <th align="left">{number}</td>
    </tr>
"""
            self.wfile.write(html.format(content).encode())




http_server=HTTPServer(('localhost',8080),WebPhonebook)
http_server.serve_forever()