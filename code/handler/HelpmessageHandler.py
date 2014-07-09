import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,dbapi
class HelpmessageHandler(tornado.web.RequestHandler):
        def post(self):
                self.write("HelpmessageHandler")
