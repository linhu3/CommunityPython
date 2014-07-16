import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class HelpmessageHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>HelpmessageHandler</p><form action='/api/helpmessage' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		#content =self.request.body
		content='{"username":"test1","message":{"kind":1,"content":"TestContent","assist":"TestAssist","latitude":123.4,"longitude":123.4}}'
		jobj=json.loads(content)
		result=self.application.dbapi.addEventByUserName(jobj["username"],jobj["message"])
		self.write(str(result))
		return