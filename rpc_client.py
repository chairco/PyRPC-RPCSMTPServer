#-*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         rpc_client.py
# Purpose:      SampleRPCClient
# Author:       Yichieh_chen
# Created:      2014.06.21
# Copyright:    (c) 1998 by Total Control Software
# Licence:      Pegartoncorp Inc. license
#----------------------------------------------------------------------------
#import modules for CGI handling

import xmlrpclib
import sys, string, os

serverip = 'http://10.193.170.242:16981'

def chk_server():
	print("Address:{0}\n".format(serverip))
	rpc_connect = xmlrpclib.ServerProxy("http://10.193.170.242:16981",allow_none=True)
	#rpc_connect = xmlrpclib.ServerProxy("http://127.0.0.1:16981")
	
	connectINFO_ret = rpc_connect.connect_INFO("user".decode("utf-8"))
	print("Server:{0}\n".format(connectINFO_ret))

def rpc(_to, _sender, _content):
	
	#rpc_connect = xmlrpclib.ServerProxy("http://172.28.144.22:16981",allow_none=True)
	rpc_connect = xmlrpclib.ServerProxy("http://10.193.170.242:16981",allow_none=True)
	#rpc_connect = xmlrpclib.ServerProxy("http://127.0.0.1:16981")
	
	connectINFO_ret = rpc_connect.connect_INFO("user".decode("utf-8"))
	print("Server:{0}\n".format(connectINFO_ret))
	
	try:
		#rpc_connect.SMTP_mail(_to.decode('big5'),_sender.decode('big5'),_content.decode('big5'))
		#(smtp_ret,mysql_ret) = rpc_connect.SMTP_mail("yichieh_chen@pegatroncorp.com","陳一傑111111111111","王小美~;%22-Q~@http")
		(smtp_ret,mysql_ret) = rpc_connect.SMTP_mail(_to,_sender,_content)
		#(smtp_ret,mysql_ret) = rpc_connect.SMTP_mail(_to.decode('big5'),_sender.decode('big5'),_content)
		print("smtp_ret = {0}".format(smtp_ret))
		print("mysql_ret = {0}".format(mysql_ret))
		
	except Exception, e:
		print(u"例外錯誤 exception error: \n")
		raise e

def readfile(filename):
	try:
		with open(filename,'r') as f:
		#f = open(filename, 'r', encoding = 'Big5')
			return f.read()   
		f.close()
	except Exception, e:
		raise e

	
def cmd():
	msg = '''\
	XMLRPC Sample program:
 	--version    : Prints the version number
 	--help       : Display this help.
 	--test       : Test server
 	--execute    : Execute the main program <select both of -c or -f>
 	 -s <sender>  : Sender
 	 -t <to>      : Mail to
 	 
 	 -c <content> : Mail content by enter
 	 -f <file>    : Mail content by file
	'''
	if len(sys.argv) < 2:
		print msg
		sys.exit()
	
	if sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option.lower() == 'version':
			print 'Version 1.00a'
		elif option.lower() == 'help': 
			print msg
		elif option.lower() == 'test':
			chk_server()
		elif option.lower() == 'execute':
			exec_count = 0			
			try:
				for i in range(len(sys.argv)):
					if sys.argv[i].upper() == '-C':
						exec_count = exec_count + 1 
						content = sys.argv[i+1][0:]
						content = content.decode('big5')
						#print(type(content))
						#print("c:"+sys.argv[i+1][0:])
					elif sys.argv[i].upper() == '-F':
						exec_count = exec_count + 1
						_file = sys.argv[i+1][0:]
						content = readfile(_file)
						#print(type(content))
						#print("f:"+content)
					elif sys.argv[i].upper() == '-T':
						exec_count = exec_count + 1
						to = sys.argv[i+1][0:]
						to = to.decode('big5')
						#print(type(to))
						#print("t:"+sys.argv[i+1][0:])
					elif sys.argv[i].upper() == '-S':
						exec_count = exec_count + 1
						sender = sys.argv[i+1][0:]
						sender = sender.decode('big5')
						#print(type(sender))
						#print("s:"+sys.argv[i+1][0:])
					else:
						pass
			except Exception, e:
				print(u"例外錯誤 exception error: \n")
				raise e
			else:
				if exec_count == 3:
					#pass
					#print(exec_count)
					rpc(to,sender,content)
				else:
					#print(exec_count)
					print 'Miss executed variable.\n' + msg
		else:
			print 'Unknown option variable.\n' + msg
		sys.exit()
	else:
	    print 'Unknown option command.\n' + msg
	
if __name__ == '__main__':
	cmd()

