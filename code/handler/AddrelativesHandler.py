import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, json, sys
sys.path.append("..")
import  dbapi


class AddrelativesHandler(tornado.web.RequestHandler):
	def post(self):
		u_name = self.get_argument('u_name')
		r_name = self.get_argument('r_name')

		row = self.application.dbapi.getRelationByUserId(u_name, r_name)
		if row == 0:
			self.application.dbapi.addRelationByUserId(u_name, r_name)
			add_message = {'state': 1}
		else:
			add_message = {'state': 0}

		self.write(add_message)
