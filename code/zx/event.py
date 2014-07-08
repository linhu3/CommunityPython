import tornado.ioloop
import tornado.web
import os,MySQLdb

class eventHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Show event page.")

	def post(self):
		userid=self.get_argument("userid")
		eventid=self.get_argument("eventid")

settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"debug": True,
}

application=tornado.web.Application([
	(r"/api/history",testHandler),
],**settings)

if __name__=="__main__":
	application.listen(8080)
	tornado.ioloop.IOLoop.instance().start()