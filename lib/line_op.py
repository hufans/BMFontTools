import os
import sys
import log

def replaceLineRight(line,key,_rep):
	_pos = line.find(key)
	if line.find(key)>=0:
		_left = line[0:_pos+len(key)]
		line = _left+_rep+"\n"
	return line;
	
def replaceLineCenter(line,left, right,_rep):
	_left_pos =  line.find(left)
	if(_left_pos < 0):
		return line
	_right_pos =  line.find(right)
	if(_right_pos < 0):
		return line
	_sub_str = line[_left_pos+len(left):_right_pos]
	_ret_val = line.replace(_sub_str,_rep)
	log.printLog("replace line:"+_sub_str+" with:"+_rep)
	return _ret_val
	
	
def replacePlistValue(lines,key,_value):
	_find = 0
	_idx = 0;
	for _line in lines:
		if _line.find(key)>0:
			break
		_idx += 1
	log.printLog("find:"+key+" line:"+str(_idx))
	_line = lines[_idx+1];
	lines[_idx+1] = replaceLineCenter(_line,"<string>","</string>",_value);
	
def getPlistValue(lines,key):
	_idx = 0;
	for _line in lines:
		if _line.find(key)>0:
			break
		_idx += 1
	log.printLog("find:"+key+" line:"+str(_idx))
	_line = lines[_idx+1];
	
	_left_pos =  _line.find("<string>")
	if(_left_pos < 0):
		return "not found"
	_right_pos =  _line.find("</string>")
	if(_right_pos < 0):
		return "not found"
	_sub_str = _line[_left_pos+len("<string>"):_right_pos]
	return _sub_str
