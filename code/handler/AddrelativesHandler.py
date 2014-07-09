import tornado.ioloop
import tornado.web
import tornado.httpserver
import os, dbapi, json, sys
sys.path.append("..")

class DeleterelativesHandler(tornado.web.RequestHandler):
    def post(self):
        cursor = dbapi.db.cursor(MySQLdb.cursors.DictCursor)
        u_id = self.get_argument('u_id')
        r_id = self.get_argument('r_id')

        cursor.execute("SELECT * FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'")
        row = int(cursor.rowcount)
        if row == 0:
            sql = "INSERT INTO relation (usrid, cid, kind) VALUES ('" + u_id + "', '" + r_id + "', '1')"
            self.write(sql)
            try:
                cursor.execute(sql)
                self.application.db.commit()
                add_message = {'state': 1}
            except:
                self.application.db.rollback()
                add_message = {'state': 2}
        else:
            add_message = {'state': 0}

            self.response.headers['Content-Type'] = "application/json"
            self.response.out.write(json.dumps(add_message))
        self.write(add_message)
