#!/usr/bin/python
# -*- coding: utf-8 -*-
import os  
import sys  
import codecs  

originUTF = open("string.txt")
str = originUTF.read()

for j in str:
  print ord(j)


originUTF.close()

