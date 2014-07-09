import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,dbapi
class LoginHandler(tornado.web.RequestHandler):
        def post(self):
                self.write("login")
