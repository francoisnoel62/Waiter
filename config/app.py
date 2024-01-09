from wsgiref.simple_server import make_server


class Waiter:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(func):
            self.routes[path] = func
            return func

        return wrapper

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            response_body = self.routes[path]()
            status = '200 OK'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return [response_body.encode()]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
            return [b'Not Found']

    def run(self, host='localhost', port=8000):
        httpd = make_server(host, port, self)
        print(f"Serving on {host}:{port}...")
        httpd.serve_forever()


app = Waiter()
