# -*- coding:utf-8 -*-
import MySQLdb
import json

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

	def regist(self):
                content = '{"username": "haha","password": 111111,"kind": 1, "cardid":11301 ,"realname":"hiii","sex":1,"age":41, "address":"iii","illness":"hijiiii"}'
                j = json.loads(content)
                cursor = self.db.cursor()
                sql = "insert into user(name,kind,password) values(%s,%s,%s)"
                param = (j["username"],j["kind"],j["password"])
                cursor.execute(sql,param)
                self.db.commit()
                print param
                return sql
    
	def __del__(self):
		self.db.close()
