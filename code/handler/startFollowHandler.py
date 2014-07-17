import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class startFollowHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>startFollowHandler</p><form action='/api/startfollow' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		content='{"id":2,"name":"ooo"}'
		j=json.loads(content)
		user=self.application.dbapi.getUserByUserName(j['name'])["id"]
		if(user):
			if(self.application.dbapi.getFollow(user["id"],j['id'])):
				data=[{'state':3}]#have  been followed
				result=json.dumps(data)
			else:
				self.application.dbapi.insertFollow(user["id"],j['id'])
				data=[{'state':1}]#start follow success
				result=json.dumps(data)
		else:
			data=[{'state':2}]#user no exist
			result=json.dumps(data)
		#return result