import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class startFollowHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>startFollowHandler</p><form action='/api/startfollow' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		content='{"uid":1,"cid":2,"kind":1,"condition":yes}'
		j=json.loads(content)
		result=self.application.dbapi.addrelation(j['uid'],j['cid'],j['conditon'],j['kind'])
		print result
		