import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class GivecreditHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>GivecreditHandler</p><form action='/api/givecredit' method='post'><input type='submit' value='submit'></form>")
	def post(self):
		#content='{"eventid":4,"helpername":"test2","credit":3}'
		content='{"eventid":1,"credits":[{"username":"test1","cridit:1},{"username":"test2","cridit":1}]}'
		jobj=json.loads(content)
		result=[]
		for issue in content['credits']:
			temp=self.application.dbapi.setCreditByEventIdAndUserName(content["eventid"],issue["username"],issue["credit"])
			result.append({"helpername":issue["username"],"result":temp});
		self.write(str(result))
		