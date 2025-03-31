class Flask(object):
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def route(self, path):
        def decorator(f):
            self.routes[path] = f
            return f
        return decorator

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "/")
        if path in self.routes:
            resp = self.routes[path]()
            start_response("200 OK", [("Content-Type", "text/html")])
            return [resp.encode("utf-8")]
        else:
            start_response("404 Not Found", [("Content-Type", "text/html")])
            return [b"Not Found"]

    def run(self, host="127.0.0.1", port=5000):
        print("Running on http://{}:{}".format(host, port))