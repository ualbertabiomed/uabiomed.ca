import tornado.websocket
import tornado.ioloop
import tornado.web

import os
import json
import logging

import app
import mail
import security


class StaticHandler(tornado.web.StaticFileHandler):
    def parse_url_path(self, url_path):
        print(url_path)
        if not url_path or url_path.endswith('/'):
            url_path = url_path + 'index.html'
        if not '.' in url_path:
            url_path = url_path + '/index.html'
        return url_path

class MessageHandler(tornado.web.RequestHandler):
    def post(self):
        memb = {}
        for x in ['name', 'email', 'msg', 'reason']:
            memb[x] = self.get_body_argument(x, default=None, strip=False)
        print(memb)
        mail.send_message("UAB Website - Contact Us Form",
                ("From: {}\nEmail: {}\nContact type: {}\nMessage:\n{}\n")
                .format(memb["name"], memb["email"], memb["reason"], memb["msg"]),
                ["uabiomed@ualberta.ca"]
            )
        self.write('<!doctype html><meta charset=utf-8><title>redirect</title><meta http-equiv="Refresh" content="0; url=/">')



application = tornado.web.Application([
    (r"/admin/?(.*)", StaticHandler, {"path": os.getcwd() + "/admin_site"}),
    (r"/message", MessageHandler),
    *app.app.endpoints(),
    (r"/(.*)", StaticHandler, {"path": os.getcwd() + "/web-bin/export"})
], debug=True)
try:
    print("server starting")
    # print(app.app.endpoints())
    application.listen(80)
    logging.getLogger('tornado.access').disabled = True # using own logger
    tornado.ioloop.IOLoop.current().start()
except KeyboardInterrupt:
    print("server exited")
