# -*- coding: utf-8 -*-
import MySQLdb,json

#in init function please change the config to fit your own requirement
#fetchone(): return type: None/dict
#fetchall(): return type: tuple(may be empty tuple)
#all function below return a value or a list

class dbapi:
	def __init__(self):
		self.host="localhost"
		self.user="comhelp"
		self.passwd="20140629"
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
	
    #check if cardid exist
	#exist return dict
	#not exist return none
	def getInfoBycardid(self,cardid):
        cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from info where cardid=%s"
		param=(cardid,)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		cursor.close()
		return result

	#register a new user
	#pre condiction:no user.name,info.cardid duplicate
	#after : insert new user,new info
	def register(self,content):
        cursor = self.db.cursor()
                
        sql = "insert into user(name,kind,password) values(%s,%s,%s)"
        param = (content["username"],content["kind"],content["password"])
        cursor.execute(sql,param)
        self.db.commit()
                
        cursor.execute('SELECT LAST_INSERT_ID()')
        result=cursor.fetchone()
        print result[0]
                
        sql = "insert into info(id,cardid,name,sex,age,address,illness,credit,score) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = (result[0],content["cardid"],content["realname"],content["sex"],content["age"],content["address"],content["illness"],0,0)
        cursor.execute(sql,param)
        self.db.commit()
                
        cursor.close()
        return

    #insert support mseeage in event
    #pre condiction:user.id，event.id exist;event.state = 0
    #after: uptate assist in event
    def supportmessageinsert(self,content):
        cursor = self.db.cursor()
        sql ="update event set assist= %s where id = %s"
        param = (content["assist"],content["eventid"])
        cursor.execute(sql,param)
        self.db.commit()
        cursor.close()
        return

	def getRelationByUserId(self, u_id, r_id):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="SELECT * FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'"
		cursor.execute(sql)
		row = int(cursor.rowcount)
		cursor.close()
		return row

	def deleteRelationByUserId(self, u_id, r_id):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="DELETE FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'"
		cursor.execute(sql)
		cursor.close()

	def addRelationByUserId(self, u_id, r_id):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="INSERT INTO relation (usrid, cid, kind) VALUES ('" + u_id + "', '" + r_id + "', '1')"
		cursor.execute(sql)
		cursor.close()

	'''Yeqin Zheng, 09/07/2014'''
	def getRelationByUserId(self, u_name, r_name):
		result = self.getUserByUserName(u_name)
		u_id = str(result["id"])
		result = self.getUserByUserName(r_name)
		r_id = str(result["id"])
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="SELECT * FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'"
		cursor.execute(sql)
		row = int(cursor.rowcount)
		cursor.close()
		return row

	def deleteRelationByUserId(self, u_name, r_name):
		result = self.getUserByUserName(u_name)
		u_id = str(result["id"])
		result = self.getUserByUserName(r_name)
		r_id = str(result["id"])
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="DELETE FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'"
		cursor.execute(sql)
		cursor.close()

	def addRelationByUserId(self, u_name, r_name):
		result = self.getUserByUserName(u_name)
		u_id = str(result["id"])
		result = self.getUserByUserName(r_name)
		r_id = str(result["id"])
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="INSERT INTO relation (usrid, cid, kind) VALUES ('" + u_id + "', '" + r_id + "', '1')"
		cursor.execute(sql)
		cursor.close()

	'''.'''

	#Anton Zhong
	def getUserIdByUserName(self,username):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select id from user where name=%s"
		param=(username,)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		cursor.close()
		return result

	def addEventByUserName(self,username,message):
		usrid=self.getUserIdByUserName(username)
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		if(not usrid):
			return {"errorCode":403,"errorDesc":"No Such User: "+username}
		else:
			if(not("kind" in message and "content" in message)):
				return {"errorCode":403,"errorDesc":"Messge Incomplete"}
			else:
				sql="insert into event (usrid,kind,state,content) values (%s,%s,%s)"
				param=(message["usrid"],0,message["content"])
				if("assist" in message):
					sql="insert into event (usrid,kind,state,content,assist) values (%s,%s,%s,%s)"
					param=(message["usrid"],0,message["content"],message["assits"])
				cursor.execute(sql,param)

				#return last insert id
				cursor.execute("select last_insert_id()")
				return {"errorCode":200,"errorDesc":"","eventid":cursor.fetchone()["last_insert_id()"]}

	#07/09

	def __del__(self):
		self.db.close()
