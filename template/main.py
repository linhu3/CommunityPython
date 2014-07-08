import tornado.ioloop
import tornado.web
import os

class testHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

	def post(self):
		print self.get_argument("username")
		self.write("Get User Name: "+self.get_argument("username"))

settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "static"),
	"debug": True,
}

application=tornado.web.Application([
	(r"/",testHandler),
],**settings)

if __name__=="__main__":
	application.listen(8080)
	tornado.ioloop.IOLoop.instance().start()