import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class cancelFollowHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>cancelFollowHandler</p><form action='/api/cancelfollow' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		content='{"id":2,"name":"ooo"}'
		j=json.loads(content)
		user=self.application.dbapi.getUserByUserName(j['name'])["id"]
		if(user):
			if(self.application.dbapi.getFollow(user["id"],j['id'])):
				self.application.dbapi.delectFollow(user["id"],j['id'])
				data=[{'state':1}]#delete follow success
				result=json.dumps(data)
			else:
				data=[{'state':3}]#have no follow
				result=json.dumps(data)
		else:
			data=[{'state':2}]#user no exist
			result=json.dumps(data)
		#return result

