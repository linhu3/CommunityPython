import MySQLdb,json

errorMsg=[
	{
		"code":0,
		"message":"success"
		"desc":""
	},
	{
		"code":1,
		"message":"fail"
		"desc":""
	}
]

class dbapi:
	def __init__(self):
		self.host="localhost"
		self.user="root"
		self.passwd="root"
		self.dbname="community"
		self.charset="utf8"
		self.db=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset=self.charset)

	#args is a json string
	def addUser(self,args):
		user=json.loads(args)
		json.dump(user)

		cursor=self.db.cursor()
		sql="""select id from user where name=%s"""
		param=(user["name"],)
		cursor.execute(sql,param)

		result=[]
		if(cursor.fetchone()){
			result=errorMsg[1]
			result["desc"]="duplicate key: "+user["name"];
		}else{
			sql="""insert into user (name,kind,info,password) values (%s,%s,%s,%s)"""
			param=(user["name"],user["kind"],user["info"],user["password"])
			cursor.execute(sql,param)
		}


	def getUserById(self,userid):
		return {}

	#Get user from table user
	def getUserByName(self,username):
		return {}

	#Update user in table user
	def updateUserByName(self,username):
		return {}

	#Update user info
	def updateUserInfoByName(self,username):
		return {}

	
	#Delete user
	def deleteUserByName(self,username):
		return {}

	#Update user info by name
	def updateUserInfoByName(self,username):
		return {}
	#Delete user info by name
	def deleteUserInfoByName(self,username):
		return {}

	#Get event By event's id
	def getEventById(self,eventid):
		cursor=self.db.cursor()
		sql="""select * from event where id=%s"""
		#Param must to tuple!
		param=(eventid,)
		cursor.execute(sql,param)
		result=cursor.fetchall()
		cursor.close()

		#Change result to dict
		result=list(result)
		re={}

		return result

	def getEventsByUserId(self,userid):
		cursor=self.db.cursor()
		cursor.close()
		return 0

	def write(self):
		return "FKU"

	def __del__(self):
		self.db.close()
