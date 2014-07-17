import tornado.ioloop
import tornado.web
import tornado.httpserver
import json
class CancelHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>CancelHandler</p><form action='/api/cancel' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		#content = self.get_argument("content")
		content = '{"username":"test","password":"test"}'
		j = json.loads(content)
		if(j['username'].strip()=='' or j['password'].strip()==''):
			self.write("{'state':1}")
			print "username or password is null,can not cancel"
			return
		user = self.application.dbapi.getUserByUserName(j['username'])
		if(user is None):
			self.write("{'state':1}")
			print "username not exist,can not cancel"
			return
		if(user["password"]!= j['password']):
			self.write("{'state':2}")
			print "passwd incorrect,can not cancel"
			return
		self.application.dbapi.cancelUser(user['id'])
		self.write("{'state':3}")
		print("cancel success")
		return
