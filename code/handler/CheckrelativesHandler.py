import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,json
class CheckrelativesHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>CheckrelativesHandler</p><form action='/api/checkrelatives' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		#content =self.request.body
		content = '{"username":"test1"}'
		j = json.loads(content)
		userid=self.application.dbapi.getUserByUserName(j['username'])["id"]
		re=self.application.dbapi.CheckRelationbyId(userid)
		if re!=():
			relatives=[]
			for row in re:
				name=self.application.dbapi.getUsermassegeByUserId(row["cid"])
				print name
				relatives.append(name)
			data={'state':1,'ralatives':str(relatives)}
		else:
			data={'state':1,'relatives':'[]'}
		self.write(data)
