# -*- coding: utf-8 -*-
import os  
import sys  
import codecs  
#import chardet
import shutil
import json
import subprocess
import lib.syscmd

def getUnicode(Line):
  local = os.getcwd()
  originUTF = open("string.txt","rb")
  configFile = open('config/config.bmfc', 'a')
  str = originUTF.read()
  #print chardet.detect(str)
  str=str.decode('utf-16')
  index = 0
  for j in str:
    lineToWrite = Line[index] +"," + unicode(ord(j)) +",0,0,0" 
    configFile.write(lineToWrite + '\n')
    index += 1 
  
  originUTF.close()
  configFile.close()

def getFilePathAndWirteTofile(picPath):
    os.chdir(os.getcwd()+"/config/") 
    fileNameOfconfig = "config.bmfc"
    shutil.copyfile("configModel.bmfc", fileNameOfconfig)
    L = []
    originUTF = open(fileNameOfconfig,"rb")
    for root, dirs, files in os.walk(path):  
        for file in files: 
          L.append("icon=\"" + root+"/"+file + '\"')

    local = os.getcwd()
    os.chdir(os.getcwd()+"/..")
    getUnicode(L)
    

def callBmFont():
    file=open(os.getcwd()+"/config/config.json",'r')
    jObj= file.read()
    jObj=jObj.decode("utf-8-sig")
    pythonObj=json.loads(jObj)
    exePath = os.getcwd() +"/BMFont/bmfont.exe"
    outPutName = pythonObj["PublishName"]
    stringName = os.getcwd() + "/" + pythonObj["stringName"]
    configName = os.getcwd() + "/config/" + pythonObj["configName"]
    strs = exePath + " -t " + stringName + " -c " + configName + " -o " +outPutName
    lib.syscmd.exec_cmd(strs)

path = os.getcwd()+ "/pic"
getFilePathAndWirteTofile(path)
callBmFont()


