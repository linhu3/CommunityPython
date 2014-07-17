import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class GetArroundEvent(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>GetArroundEvent</p><form action='/api/getAround' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		#content =self.request.body
		content='{"username":"test1"}'
		j=json.loads(content)
		user = self.application.dbapi.getUserAllinfobyName(j['username'])
		if(user is None):
			self.write("{'state':2}")
			print "username not exist"
			return
		result = self.application.dbapi.getUserAround(user['longitude'],user['latitude'],150)
		self.write("{'state':1,aids:"+str(result)+"}")
		return
