#encoding=utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import MySQLdb
import json
import re

from tornado.options import define, options
define("port", default=8030, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/api/deleterelatives/u_id=([0-9]+)&r_id=([0-9]+)", DeleteRelatives),
                    (r"/api/addrelatives/u_id=([0-9]+)&r_id=([0-9]+)", AddRelatives)]
        self.db = MySQLdb.connect(host='localhost',user='comhelp',passwd='20140629',db="community",charset='utf8')
        tornado.web.Application.__init__(self, handlers, debug=True)

class DeleteRelatives(tornado.web.RequestHandler):
    def get(self, u_id, r_id):
        cursor = self.application.db.cursor(MySQLdb.cursors.DictCursor)
        #self.write(u_id + r_id)
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

class AddRelatives(tornado.web.RequestHandler):
    def get(self, u_id, r_id):
        cursor = self.application.db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'")
        row = int(cursor.rowcount)
        if row == 0:
            sql = "INSERT INTO relation (usrid, cid, kind) VALUES ('" + u_id + "', '" + r_id + "', '1')"
            #self.write(sql)
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

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()