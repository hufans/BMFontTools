import httplib
from urlparse import urlparse
import socket 
import struct 
import log
import os
import json

local_path = os.path.dirname(__file__)
if local_path=="":
	local_path = os.getcwd()
	
def post_data(_url,_data):
	log.printLog("POST:"+_url)
	#log.printLog("Data:"+_data)
	url_data = urlparse(_url)
	#print 'protocol:',url_data.scheme
	#print 'hostname:',url_data.hostname
	#print 'port:',url_data.port
	#print 'path:',url_data.path
	
	hostname = url_data.hostname
	if  url_data.port:
		hostname += ":"+str(url_data.port)
	#log.printLog("hostname:"+hostname)
	
	#headerdata = {"Content-Length":len(reqData)}
	headerdata = {}
	try:
		conn = httplib.HTTPConnection(hostname)
		conn.request(method="POST",url=url_data.path,body=_data,headers = headerdata) 
		response = conn.getresponse()
		res= response.read()
		log.printLog(res)
		return res
	except :
		log.printLog("POST_ERROR!")
		
def put_data(_url,_data):
	log.printLog("PUT:"+_url)
	#log.printLog("Data:"+_data)
	url_data = urlparse(_url)
	
	hostname = url_data.hostname
	if  url_data.port:
		hostname += ":"+str(url_data.port)
	#log.printLog("hostname:"+hostname)
	
	#headerdata = {"Content-Length":len(reqData)}
	headerdata = {}
	try:
		conn = httplib.HTTPConnection(hostname)
		conn.request(method="PUT",url=url_data.path,body=_data,headers = headerdata) 
		response = conn.getresponse()
		log.printLog("RESP STATUS:"+str(response.status))
		res= response.read()
		log.printLog(res)
		return res
	except :
		log.printLog("PUT_ERROR!")


def get_local_host(): 
	#hostname = socket.getfqdn(socket.gethostname())
	#print("host name:"+hostname)
	#addr = socket.gethostbyname(hostname)
	#return addr
	log.printLog("get local ip from console_config.json")
	console_config = local_path+"/../../../console_config.json"
	with open(console_config) as f:
		config = json.load(f)
		return "http://"+config["local_ip"]+":"+str(config["local_port"])+"/"
	
if __name__ == "__main__":
	print get_local_ip() 