import os
import sys
import log
import subprocess

def exec_cmd(cmd):
	
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	#ret_code = process.wait()
	result = process.stdout.read()
	#log.printLog(result)
	
	error = process.stderr.read()
	if error and error != "":
		log.printLog("execute cmd:"+cmd+" eror!")
		log.printLog(error)
		return result+error
	return result