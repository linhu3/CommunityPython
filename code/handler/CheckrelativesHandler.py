import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
class CheckrelativesHandler(tornado.web.RequestHandler):
        def post(self):
		#username=self.get_argument("content")
		content = '{"username": "ooo"}'
		j = json.loads(content)
		userid=self.application.dbapi.getUserByUserName(j['username'])["id"]
		re=self.application.dbapi.CheckRelationbyId(userid)
		if re!=():
			relatives=[]
			for row in re:
				name=self.application.dbapi.getUsermassegeByUserId(row["cid"])
				relatives.append(name)
			data1=[{'state':1},relatives]
			data=json.dumps(data1)
		else:
			data1=[{'state':0}]
			data=json.dumps(data1)
		self.write(data)
