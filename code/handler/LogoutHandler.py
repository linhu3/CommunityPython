import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,dbapi
class LogoutHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>LogoutHandler</p><form action='/api/logout' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		self.write("LogoutHandler")
