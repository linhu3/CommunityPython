import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,dbapi
class AddaidHandler(tornado.web.RequestHandler):
		def post(self):
				self.write("<p>AddaidHandler</p><form action='/api/history' method='post'><input type='submit' value='submit'></form>")
