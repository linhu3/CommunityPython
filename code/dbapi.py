# -*- coding: utf-8 -*-
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

	def updateUserstate(self,uid,state):
		cursor = self.db.cursor()
		sql = "update user set state = %s where id = %s"
		param =(state,uid)
		cursor.execute(sql,param)
		self.db.commit()
		cursor.close()
		return

	#get user all info in user+info
	#pre con: user exist
	#after: return a dict result include all info of user
	def getUserAllinfobyName(self,name):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		uid = self.getUserByUserName(name)['id']
		return self.getUsermassegeByUserId(uid)

	def CheckRelationbyId(self,userid):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from relation where usrid=%s"
		param=(userid,)
		cursor.execute(sql,param)
		result=cursor.fetchall()
		cursor.close()
		return result

	def getUsermassegeByUserId(self,userid):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from user ,info where user.id=%s and info.id=%s"
		param=(userid,userid)
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
		return self.getEventsByUserId(user["id"])

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

	#update user cid by uid
	def UpdateCidByuid(self,cid,uid):
		cursor = self.db.cursor()
		sql = "update user set cid = %s where id = %s"
		param = (cid,uid)
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

    #get all relativeName by user.id
    #return a list contain all relations(including uid)
	def getAllRelativeNamebyUid(self,uid):
		cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql = "select * from relation where usrid = %s"
		param = (uid,)
		rlist = []
		rlist.append(uid)
		cursor.execute(sql,param)
		for row in cursor.fetchall():
			rlist.append(row["cid"])
		return rlist

	# change a event sate to 1
	#in order to end a event
	def changeEventState(self,eid):
		cursor = self.db.cursor()
		sql ="update event set state= %s where id = %s"
		param = (1,eid)
		cursor.execute(sql,param)
		self.db.commit()
		cursor.close()
		return

	#cancle a user by user(id)
	#pre condiction: uid exist
	#after:delete all record of this user
	def cancelUser(self,uid):
		cursor = self.db.cursor()
		sql = "delete from user where id = %s"
		param = (uid,)
		cursor.execute(sql,param)
		self.db.commit()
		cursor.close()
		return

	#get all events around user(latitude,longitude) inside distance
	#pre con:user(latitude,longitude) exist,distance >=0
	#after:return a list contain event info or []
	def getEventAround(self,lon,lat,distance):
		cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		#sql = "select round(6378.138*2*asin(sqrt(pow(sin( (event.latitude*pi()/180-(%s)*pi()/180)/2),2)+cos(event.latitude*pi()/180)*cos((%s)*pi()/180)* pow(sin( (event.longitude*pi()/180-(%s)*pi()/180)/2),2)))) from event"
		#param = (lat,lat,lon)
		sql = """select event.id,user.name,event.kind,event.content,event.assist,event.starttime from event,user where 
				 exists(select id from event where event.latitude <= (%s+1) and event.latitude >= (%s-1) and longitude <= (%s+1) and longitude>=(%s-1))
				 and event.usrid = user.id
				 and event.state = 0
				 and round(6378.138*2*asin(sqrt(pow(sin( (event.latitude*pi()/180-(%s)*pi()/180)/2),2)+cos(event.latitude*pi()/180)*cos((%s)*pi()/180)* pow(sin( (event.longitude*pi()/180-(%s)*pi()/180)/2),2)))) < %s """
		param = (lat,lat,lon,lon,lat,lat,lon,distance)
		cursor.execute(sql,param)
		result = []
		for row in cursor.fetchall():
			result.append(row)
		cursor.close()
		return result

	#get all user(cid) around latitude,longitude inside distance(use for push)
	#pre condiction：lon,lat exist,distance>=0
	#after :return a list coantain user.cid or []
	def getUserCidAround(self,lon,lat,distance):
		cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql = """select user.cid from user,info where
				exists(select id from info where latitude <= (%s+1) and latitude >= (%s-1) and longitude <= (%s+1) and longitude>=(%s-1))
				and user.state = 1
				and user.id = info.id
				and round(6378.138*2*asin(sqrt(pow(sin( (info.latitude*pi()/180-(%s)*pi()/180)/2),2)+cos(info.latitude*pi()/180)*cos((%s)*pi()/180)* pow(sin( (info.longitude*pi()/180-(%s)*pi()/180)/2),2)))) < %s"""
		param = (lat,lat,lon,lon,lat,lat,lon,distance)
		cursor.execute(sql,param)
		result = []
		for row in cursor.fetchall():
			result.append(row)
		cursor.close()
		return result

	'''Yeqin Zheng, 09/07/2014'''
	def getRelationByUsername(self, u_name, r_name):
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

	def deleteRelationByUsername(self, u_name, r_name):
		result = self.getUserByUserName(u_name)
		u_id = str(result["id"])
		result = self.getUserByUserName(r_name)
		r_id = str(result["id"])
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="DELETE FROM relation WHERE usrid = '" + u_id + "' AND cid = '" + r_id + "'"
		cursor.execute(sql)
		self.db.commit()
		cursor.close()

	def addRelationByUsername(self, u_name, r_name):
		result = self.getUserByUserName(u_name)
		u_id = str(result["id"])
		result = self.getUserByUserName(r_name)
		r_id = str(result["id"])
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="INSERT INTO relation (usrid, cid, kind) VALUES ('" + u_id + "', '" + r_id + "', '1')"
		cursor.execute(sql)
		self.db.commit()
		cursor.close()

	def addaidhelper(self, u_name, e_id):
		result = self.getUserByUserName(u_name)
		u_id = str(result["id"])
		result = self.getEventByEventId(e_id)
		if(self.checkifUseraddHelper(u_id,e_id) is not None):
			print "already add in,do not need add agagin"
			return "2"
		if result["state"] == 1:
			print "current has benn end"
			return "3"
		else:
			cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql="INSERT INTO helper (eid, usrid) VALUES ('" + e_id + "', '" + u_id + "')"
			cursor.execute(sql)
			self.db.commit()
			cursor.close()
			print "user " +u_name +" add in "+ e_id
			return "1"

	def checkifUseraddHelper(self,userid,eventid):
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from helper where eid=%s and usrid = %s"
		param=(eventid,userid)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		print result
		return result

	def deleteHelperbyUidEid(self,uid,eid):
		cursor=self.db.cursor()
		sql="delete from helper where eid = %s and usrid = %s"
		param=(eid,uid)
		cursor.execute(sql,param)
		self.db.commit()
		cursor.close()
		return


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
			return {"state":2,"errorDesc":"No Such User: "+username}
		else:
			if(not("kind" in message and "content" in message)):
				return {"state":3,"errorDesc":"Messge Incomplete"}
			else:
				sql="insert into event (usrid,kind,state,content) values (%s,%s,%s,%s)"
				param=(usrid["id"],message["kind"],0,message["content"])
				if("assist" in message):
					sql="insert into event (usrid,kind,state,content,assist) values (%s,%s,%s,%s,%s)"
					param=(usrid["id"],message["kind"],0,message["content"],message["assist"])
				cursor.execute(sql,param)
				self.db.commit()

				#return last insert id
				cursor.execute("select last_insert_id()")
				return {"state":1,"errorDesc":"","eventid":cursor.fetchone()["last_insert_id()"]}
		cursor.close()

	#07/09

	#Anton Zhong
	def getHelperByEventIdAndUserName(self,eid,username):
		usrid=self.getUserIdByUserName(username)
		#No such user return none
		if(not usrid):
			return None
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select * from helper where eid=%s and usrid=%s"
		param=(eid,usrid["id"])
		cursor.execute(sql,param)
		result=cursor.fetchone()
		cursor.close()
		return result

	def checkHelperByEventIdAndUserName(self,eid,username):
		usrid=self.getUserIdByUserName(username)
		if(not usrid):
			return False
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="select usrid from helper where eid=%s"
		param=(eid,)
		cursor.execute(sql,param)
		result=cursor.fetchone()
		if(not result):
			return False
		return True

	def addSupportByEventIdAndUserName(self,eid,username,message):
		if(not self.checkHelperByEventIdAndUserName(eid,username)):
			return {"errorCode":403,"errorDesc":"No Such Helper "+str(username)+" in event "+str(eid)}
		if(not ("content" in message) ):
			return {"errorCode":403,"errorDesc":"Messge Incomplete"}
		else:
			cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
			sql="insert into support (eid,usrid,content) values (%s,%s,%s)"
			param=(eid,self.getUserIdByUserName(username)["id"],message["content"])
			cursor.execute(sql,param)
			self.db.commit()
			cursor.execute("select last_insert_id()")
			result=cursor.fetchone()
			cursor.close()
			return {"errorCode":200,"errorDesc":"","supportid":result["last_insert_id()"]}

	def setCreditByEventIdAndUserName(self,eid,username,credit):
		if(not self.checkHelperByEventIdAndUserName(eid,username)):
			return {"errorCode":403,"errorDesc":"No Such Helper "+str(username)+" in event "+str(eid)}
		cursor=self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		sql="update helper set credit = %s where eid=%s and usrid=%s"
		usrid=self.getUserIdByUserName(username)
		param=(credit,eid,usrid["id"])
		cursor.execute(sql,param)
		self.db.commit()
		cursor.close()
		return {"errorCode":200,"errorDesc":""}
	#07/10

	def __del__(self):
		self.db.close()
