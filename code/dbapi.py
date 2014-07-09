import MySQLdb,json

#in init function please change the config to fit your own requirement
#fetchone(): return type: None/dict
#fetchall(): return type: tuple(may be empty tuple)
#all function below return a value or a list

class dbapi:
	def __init__(self):
		self.host="localhost"
		self.user="root"
		self.passwd="root"
		self.dbname="community"
		self.charset="utf8"
		self.db=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset=self.charset)

	def getUserByUserId(self,userid):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from user where id=%s"
		param=(userid,)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		cursor.close()
		return result

	def getUserByUserName(self,username):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from user where name=%s"
		param=(username,)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		cursor.close()
		return result

	def getEventByEventId(self,eventid):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from event where id=%s"
		param=(eventid,)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		cursor.close()
		return result

	def getEventsByUserId(self,userid):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from event where usrid=%s"
		param=(userid,)
		cursor.execute(sql,param)
		result=cursor.fetchall()
		cursor.close()
		return list(result)

	def getEventsByUserName(self,username):
		user=self.getUserByUserName(username)
		if(not user):
			return []
		return self.getEventsByUserId(user["userid"])

	def __del__(self):
		self.db.close()
