"""
A simple tornado routing package
Written by Jacob and Peter
"""

import re
import time
import tornado.web
import json

import security



class PocketTornado():
    ACCEPTED = 'ok'
    UNDEFINED = "undefined"
    UNAUTHORIZED = "unauth"
    def __init__(self, secret="secret", timeout=60*60):
        self.funcs = {}
        self.handlers = []
        self.authorizers = set() # api calls that authorize if they succed
        self.authorized = set() # api calls that must be authorized
        self.secret = secret
        self.timeout = timeout

    def listen(self, port, debug=False):
        app = self.createApp(debug)
        app.listen(port)
        tornado.ioloop.IOLoop.current().start()

    def replaceStrings(self, path):
        path = re.sub("/", r"/", path)
        path = re.sub("<int>", "(\\\\d+)", path)
        path = re.sub("<string>", "([^\\/]+)", path)
        path = re.sub("<all>", "(.*)", path)
        path += "\\/?"
        return path

    def apifunction(self, path, verb, content_type):
        path = self.replaceStrings(path)

        def holder(func):
            if path not in self.funcs:
                self.funcs[path] = {}
            self.funcs[path][verb] = func
            self.funcs[path][verb].content_type = content_type
            return func
        return holder

    def get(self, path, content_type=UNDEFINED):
        return self.apifunction(path, "get", content_type)

    def post(self, path, content_type=UNDEFINED):
        return self.apifunction(path, "post", content_type)

    def delete(self, path, content_type=UNDEFINED):
        return self.apifunction(path, "delete", content_type)

    def put(self, path, content_type=UNDEFINED):
        return self.apifunction(path, "put", content_type)

    def secure(self, func):
        self.authorized.add(func)
        return func

    def makeSecure(self, func):
        self.authorizers.add(func)
        return func

    def static(self, webpath, localpath, remap={}, append_file_type=".html"):
        webpath = self.replaceStrings(webpath)
        print(webpath)
        a = tornado.web.StaticFileHandler
        fmap = {}
        for key in remap.keys():
            if key.endswith("/"):
                if key == "/":
                    fmap[""] = remap[key]
                fmap[key[:-1]] = remap[key]
            else:
                fmap[key + "/"] = remap[key]

        for key in fmap.keys():
            remap[key] = fmap[key]

        def fun(self, path):
            if not path.contains("."):
                path += append_file_type
            if path in remap:
                return remap[path]
            return path

        a.parse_url_path = fun

        self.funcs[webpath] = ((a, {'path': localpath}))

        def wrap(func):
            return func
        return wrap

    def endpoints(self):
        for path in sorted(
                self.funcs.keys(),
                reverse=True):  # this ensures \/(.*)\/? is at the end
            print(f"Path: {path}")
            if isinstance(self.funcs[path], tuple):
                self.handlers.append((path, *self.funcs[path]))
                continue
            self.handlers.append((path, self.handler(
                self.funcs[path]
            )))
        return self.handlers

    def handler(superself, methods):
        class tornadoHandler(tornado.web.RequestHandler):
            def set_default_headers(self):

                self.set_header("Access-Control-Allow-Origin", "*")
                self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
                self.set_header(
                    'Access-Control-Allow-Methods',
                    ', '.join([s.upper() for s in methods]) + ", OPTIONS")

            def options(self, *args, **kwargs):
                self.set_status(204)
                self.finish()

        for method in methods:
            setattr(
                tornadoHandler,
                method,
                superself.newwrapper(
                    methods[method],
                    method,
                    methods[method].content_type))
        return tornadoHandler

    def newwrapper(self, func, verb, content_type):
        pt = self
        ttime = 0
        def wrapper(self, *args):
            now = time.time()
            ttime = now
            try:
                output = ""
                if output == "":
                    if verb in ("post", "put"):
                        output = func(
                            json.loads(self.request.body.decode("utf-8")),
                            *args
                        )
                    elif verb in ("get", "delete"):
                        output = func(*args)


                if output == PocketTornado.ACCEPTED:
                    self.set_header("Content-Type", "text/plain")
                    self.set_status(202)
                    self.finish("202: Accepted")
                elif output == PocketTornado.UNAUTHORIZED:
                    self.set_header("Content-Type", "text/plain")
                    self.set_status(401)
                    self.finish()
                elif output is None:
                    self.set_header("Content-Type", "text/plain")
                    self.set_status(204)
                    self.finish()
                else:
                    self.write(output)
                    if content_type != PocketTornado.UNDEFINED:
                        self.set_header("Content-Type", content_type)
            except (KeyError, json.decoder.JSONDecodeError, Error400):
                self.set_header("Content-Type", "text/plain")
                self.set_status(400)
                self.finish("400: Bad Request")
            except Error404:
                self.set_header("Content-Type", "text/plain")
                self.set_status(404)
                self.finish("404: Not Found")
            prettyPrintServerMessage(
                self._status_code,
                verb,
                self.request.path,
                self.request.remote_ip,
                ((time.time() - ttime) * 1000))

        return wrapper

    def createApp(self, debu):
        return tornado.web.Application([
            *self.endpoints(),
        ], debug=debu)


def prettyPrintServerMessage(status, verb, path, ip, time):

    col = None
    if 200 <= status and status < 300:
        col = colourPrinter.green
    elif 300 <= status and status < 400:
        col = colourPrinter.yellow
    elif 400 <= status:
        col = colourPrinter.red

    verbColours = {
        "GET": colourPrinter.green,
        "POST": colourPrinter.blue,
        "PUT": colourPrinter.yellow,
        "DELETE": colourPrinter.red
    }

    verbColour = colourPrinter.setColour(verbColours[verb.upper()])

    if time < 1000:
        timeColour = colourPrinter.setColour(colourPrinter.green)
    elif time < 5 * 1000:
        timeColour = colourPrinter.setColour(colourPrinter.yellow)
    else:
        timeColour = colourPrinter.setColour(colourPrinter.red)

    statusColour = ""
    normal = colourPrinter.resetColour()
    if col is not None:
        statusColour = colourPrinter.setColour(colourPrinter.black, col)

    print((statusColour +
           "|{4}|" +
           normal +
           ": " +
           verbColour +
           "{0}" +
           normal +
           " {1} ({2}) " +
           timeColour +
           "{3:.2f}ms" +
           normal).format(verb.upper(), path, ip, time, str(status)))


class colourPrinter():
    black = 0
    red = 1
    green = 2
    yellow = 3
    blue = 4
    magenta = 5
    cyan = 6
    white = 7

    @staticmethod
    def setColour(forground=white, background=black):
        return "\033[3{};4{}m".format(forground, background)

    @staticmethod
    def resetColour():
        return "\033[0m"


class Error404(Exception):
    pass


class Error400(Exception):
    pass
