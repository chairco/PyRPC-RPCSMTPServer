#!/usr/bin/python 
#-*- coding: utf-8 -*-
import SimpleXMLRPCServer
from smtp.pegaSMTP import SMTPServer
from smtp.db_insert import mysql
import string

def connect_INFO(sMsg): #從遠端呼叫並且帶入參數
	print "Connect success, HI %s" % sMsg
	return "Connect success"

def SMTP_mail(to, sender, content):

	_to = to
	_sender = sender
	_content = content
	_ip = "0.0.0.0"

	#print(type(_to))
	#print(type(_sender))
	#print(type(_content))

	if isinstance(_to, unicode):
		_to = _to.encode('utf-8')
	if isinstance(_sender, unicode):  
		_sender = _sender.encode('utf-8')
	if isinstance(_content, unicode):
		_content = _content.encode('utf-8')
	
	#///smtp 
	try:
	 	smt_ret = SMTPServer("bg3_ptd@pegatroncorp.com",_to,_content + " by " +_sender)
	 	
	 	#///mysql
	 	try:
	 		mysql_ret = mysql(_sender, _ip, _content, "0", _to)
	 		ret = [smt_ret,mysql_ret]
	 		return ret
	 	
	 	except Exception, e:
	 		print("MySQL FAIL: \n{0}".format(e))
			return e.args
	
	except Exception, e:
	 	print("SMTP Server FAIL: \n{0}".format(e))
		return e.args

def main():
	serverIP = "172.28.144.22"
	#serverIP = "127.0.0.1"
	#serverIP = "10.193.170.242"

	server = SimpleXMLRPCServer.SimpleXMLRPCServer((serverIP, 16981))
	server.register_function(connect_INFO)  #將 connect_INFO 的function 註冊為可以讓 Client 呼叫的 function
	server.register_function(SMTP_mail)
	print("Start RPC Server...!!")
	server.serve_forever() #Server Start, 開始等待訊息

if __name__ == '__main__':
	main()
	sys.exit()

