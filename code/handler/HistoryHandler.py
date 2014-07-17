import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class HistoryHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>historyHandler</p><form action='/api/history' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		content='{"id":2,"name":"ooo"}'
		jobj=json.loads(content)
		events=self.application.dbapi.getEventsByUserId(jobj['id'])
		#result=self.application.dbapi.getEventsByUserName(jobj['name'])
		supports = self.application.dbapi.getSupportsbyUid(jobj['id'])

		self.write('{events:'+str(events)+',"supports":'+str(supports))