import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import MySQLdb

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class Application(tornado.web.Application):
	def _init_(self):
		handlers=[(r"/api/cancel",cancel),(r"/api/relatives",relatives)]
		tornado.web.Application._init_(self,handlers,debug=True)

connection=MySQLdb.connect(user='root',db='abc',host='localhost',port=3306,charset='utf8')
cur=connection.cursor()
 

class cancel(tornado.web.RequestHandler):
	def post(self):		
		name=self.get_argument('username')
		cur.execute('select id from user where name=user.name')
		result1=cur.fetchone()
		sql="delete from info where result1=info.id"
		param=("aaa")
		n=cur.execute(sql,param)
		sql="delete from user where name=user.name"
		param=("aaa")
		n=cur.execute(sql,param)
		self.write(n)

class checkrelatives(tornado.web.RequestHandler):
	def post(self):
		name=self.get_argument('username')
		cur.execute('select id from user where name=user.name')
		result1=cur.fetchone()
		cur.execute('select cid from relation where result1=relation.usrid')
		result2=cur.fetchall()
		cur.execute('select * from user full join info on result2=user.id and result2=info.id')
		result3=cur.fetchall()
		self.write(result3)

cur.close()
connection.close()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app=Application(handlers)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()