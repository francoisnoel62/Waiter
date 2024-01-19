from http import HTTPStatus
import json
import logging
from wsgiref.simple_server import make_server
import re

from config.customs_exceptions import ObjectDoesNotExistsException

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Waiter:
    def __init__(self):
        self.routes = []

    def get(self, path):
        def wrapper(func):
            # Convert route path to a regex pattern
            pattern = re.sub(r'{(.*?)}', r'(?P<\1>[^/]+)', path)
            self.routes.append(('GET', re.compile(f"^{pattern}$"), func))
            return func

        return wrapper

    def post(self, path):
        def wrapper(func):
            # Convert route path to a regex pattern
            pattern = re.sub(r'{(.*?)}', r'(?P<\1>[^/]+)', path)
            self.routes.append(('POST', re.compile(f"^{pattern}$"), func))
            return func

        return wrapper

    def delete(self, path):
        def wrapper(func):
            # Convert route path to a regex pattern
            pattern = re.sub(r'{(.*?)}', r'(?P<\1>[^/]+)', path)
            self.routes.append(('DELETE', re.compile(f"^{pattern}$"), func))
            return func

        return wrapper

    def put(self, path):
        def wrapper(func):
            # Convert route path to a regex pattern
            pattern = re.sub(r'{(.*?)}', r'(?P<\1>[^/]+)', path)
            self.routes.append(('PUT', re.compile(f"^{pattern}$"), func))
            return func

        return wrapper

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        for registered_method, pattern, handler in self.routes:
            if registered_method == method:
                match = pattern.match(path)
                if match:
                    # Extract path parameters from the match object
                    params = match.groupdict()
                    print(params)

                    if method == 'POST' or method == 'PUT':
                        # Handle POST request with JSON data
                        content_length = int(environ.get('CONTENT_LENGTH', 0))
                        if content_length > 0:
                            post_data = environ['wsgi.input'].read(content_length)
                            try:
                                post_data = json.loads(post_data.decode())
                            except json.JSONDecodeError:
                                start_response('400 BAD REQUEST', [('Content-Type', 'text/plain')])
                                return [b'Invalid JSON data']
                            params['contact'] = post_data

                    if method == 'GET':
                        try:
                            response_body = handler(**params)
                            status = str(HTTPStatus.OK.value) + ' ' + HTTPStatus.OK.phrase
                            headers = [('Content-type', 'application/json')]
                            start_response(status, headers)
                            return [response_body.encode('utf-8')] if isinstance(response_body, str) else [
                                json.dumps(response_body).encode('utf-8')]
                        except ObjectDoesNotExistsException as e:
                            print(e)
                            error_response = {'error': str(e)}
                            start_response(str(HTTPStatus.NO_CONTENT.value) + ' ' + HTTPStatus.NO_CONTENT.phrase,
                                           [('Content-Type', 'application/json')])
                            return [json.dumps(error_response, indent=4).encode('utf-8')]

        # No matching route found
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return [b'Not Found']

    def run(self, host='localhost', port=8000):
        httpd = make_server(host, port, self)
        print(f"Serving on {host}:{port}...")
        httpd.serve_forever()


# Create an instance of the Waiter class
app = Waiter()
