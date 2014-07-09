import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, dbapi, json, sys
sys.path.append("..")

class DeleterelativesHandler(tornado.web.RequestHandler):
    def post(self):
        cursor = dbapi.db.cursor(MySQLdb.cursors.DictCursor)
        #self.write(u_id + r_id)
        u_id = self.get_argument('u_id')
        r_id = self.get_argument('r_id')

        cursor.execute("SELECT * FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'")
        row = int(cursor.rowcount)
        #self.write(row2)
        if row == 0 :
            delete_message = {'state': 0}
        else :
            cursor.execute("DELETE FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'")
            row = int(cursor.rowcount)
            delete_message = {'state': 1}

            self.response.headers['Content-Type'] = "application/json"
            self.response.out.write(json.dumps(delete_message))
        self.write(delete_message)
