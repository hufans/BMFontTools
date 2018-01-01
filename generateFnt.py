# -*- coding: utf-8 -*-
import os  
import sys  
import codecs  
import chardet

originUTF = open("string.txt","rb")
str = originUTF.read()
print chardet.detect(str) 
str=str.decode('utf-16')
for j in str:
  print ord(j)

originUTF.close()

