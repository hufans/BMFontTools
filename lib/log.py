import os
import sys
import shutil
import datetime
import json

local_path = os.path.dirname(__file__)

log_file_path = local_path+"font_log.txt"
logFile = open(log_file_path,'a+')

def clear_log():
	global logFile
	logFile.close()
	if os.path.exists(log_file_path):
		os.remove(log_file_path)
	logFile = open(log_file_path,'a+')

def printLog(str):
	global logFile
	print(str)
	time = datetime.datetime.now().strftime('[%m-%d %H:%M:%S]')
	_log = time+str+"\n"
	logFile.write(_log)
	logFile.flush()
	