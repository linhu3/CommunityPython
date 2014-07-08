import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,MySQLdb,dbapi

#Change the handler class and make it to fit your requirement
class historyHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

	def post(self):
		username=self.get_argument("username")
		print self.application.dbapi.getEventById(1)

class app(tornado.web.Application):
	def __init__(self):
		settings={
			"static_path": os.path.join(os.path.dirname(__file__), "static"),
			"debug": True,
		}
		handlers=[(r"/api/history",historyHandler),]
		tornado.web.Application.__init__(self,handlers,**settings)
		self.dbapi=dbapi.dbapi()
		

if __name__=="__main__":
	server=tornado.httpserver.HTTPServer(app())
	server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()