import MySQLdb

class dbapi:
	def __init__(self):
		#Change the database config to fit you own pc
		self.host="localhost"
		self.user="root"
		self.passwd="root"
		self.dbname="community"
		self.charset="utf8"
		self.db=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset=self.charset)

	#Get event By event's id
	def getEventById(self,eventid):
		cursor=self.db.cursor()
		sql="""select * from event where id=%s"""
		#Param must to tuple!1
		param=(eventid,)
		cursor.execute(sql,param)
		result=cursor.fetchall()
		cursor.close()
		return result

	def getEventsByUserId(self,userid):
		cursor=self.db.cursor()
		cursor.close()
		return 0

	def write(self):
		return "FKU"

	def __del__(self):
		self.db.close()
