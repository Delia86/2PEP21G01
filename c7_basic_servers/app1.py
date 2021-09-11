import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler


with open('index.html') as file:

    html = file.read()

phone_book = {'key1': 1}


class WebPhoneBook(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        content = ''
        for name, number in phone_book.items():
            content += f"""
    <tr>
        <td align="left">{name}</td>
        <td align="left">{number}</td>
    </tr>
"""
        self.wfile.write(html.format(content).encode())

    def do_POST(self):
        if self.path.endswith('/add'):
            # content_type,data=cgi.parse_header(self.headers.get('content-type'))
            # print(content_type,data)
            # data['boundary']=bytes(data['boundary'],'utf-8')
            # c_len=int(self.headers.get('Content-length'))
            # data['CONTENT-LENGTH']=c_len
            print('content',cgi.parse(self.rfile))

            # print(self.headers.get('content-type'))

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_DELETE(self):
        if self.path.endswith('/add'):
            print('Remove')
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()


http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
http_server.serve_forever()