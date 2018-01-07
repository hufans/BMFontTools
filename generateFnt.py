# -*- coding: utf-8 -*-
import os  
import sys  
import codecs  
#import chardet
import shutil

def getUnicode(Line):
  originUTF = open("string.txt","rb")
  configFile = open('config.bmfc', 'a')
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
    fileNameOfconfig = "config.bmfc"
    shutil.copyfile("configModel.bmfc", fileNameOfconfig)
    L = []
    originUTF = open(fileNameOfconfig,"rb")
    for root, dirs, files in os.walk(path):  
        for file in files: 
          L.append("icon=\"" + root+"/"+file + '\"')

    getUnicode(L)

def callBmFont():
      with open("config.json",'r') as load_f:
      load_dict = json.load(load_f)
      exePath = load_dict.BMFont_PATH,
      os.system(exePath)

path = os.getcwd()+ "/pic"
getFilePathAndWirteTofile(path)
callBmFont()


