import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,dbapi
class SupportmessageHandler(tornado.web.RequestHandler):
        def post(self):
                self.write("SupportmessageHandler")
