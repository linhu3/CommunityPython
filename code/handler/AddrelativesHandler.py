import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, json, sys
sys.path.append("..")
import  dbapi

class AddrelativesHandler(tornado.web.RequestHandler):
    def post(self):
        u_id = self.get_argument('u_id')
        r_id = self.get_argument('r_id')

        row = self.application.dbapi.getRelationByUserId(u_id, r_id)
        if row == 0:
            self.application.dbapi.addRelationByUserId(u_id, r_id)
            add_message = {'state': 1}
        else:
            add_message = {'state': 0}

        self.write(add_message)
