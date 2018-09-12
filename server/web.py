import tornado.websocket
import tornado.ioloop
import tornado.web

import os

domain_name = "http://localhost:8000"

class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return origin.startswith(domain_name)

    def open(self):
        print("new client")

    def on_message(self, data):
        print(data)

    def on_close(self):
        print("a client left")

class StaticHandler(tornado.web.StaticFileHandler):
    def parse_url_path(self, url_path):
        if not url_path or url_path.endswith('/'):
            url_path = url_path + 'index.html'
        if not '.' in url_path:
            url_path = url_path + '.html'
        return url_path

class JoinHandler(tornado.web.RequestHandler):
    def post(self):
        memb = {}
        for x in ['name', 'email', 'msg']:
            memb[x] = self.get_body_argument(x, default=None, strip=False)
        print(self.request)
        print(memb)
        self.write('<!doctype html><meta charset=utf-8><title>redirect</title><meta http-equiv="Refresh" content="0; url=/">')

application = tornado.web.Application([
    (r"/websocket", SocketHandler),
    (r"/iamanewmember", JoinHandler),
    (r"/iamanewsponsor", JoinHandler),
    (r"/(.*)", StaticHandler, {"path": os.getcwd() + "/site/bin"})
], debug=True)

try:
    print("server starting")
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
except KeyboardInterrupt:
    print("server exited")
