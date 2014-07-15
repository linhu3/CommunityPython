# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.httpserver
import json

class UpdateCid(tornado.web.RequestHandler):
	def get(self):
		self.write("<p>UpdateCid</p><form action='/api/updatecid' method='post'><input type='submit' value='submit'></form>")

	def post(self):
		#content =self.request.body
		content = '{"username":"test1","cid":"dasdada"}'
		j = json.loads(content)
		user = self.application.dbapi.getUserByUserName(j['username'])
		if(user is None):
			self.write("{'state':2}")
			print "username not exist"
			return
		self.application.dbapi.UpdateCidByuid(j['cid'],user['id'])
		self.write("{'state':1}")
		print("Login success")
		return