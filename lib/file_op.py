import os
import sys
import shutil
import log
import binascii
_suffix = ".tmp"

def readTextLines(full_path):
	f = open(full_path,"r")
	lines = f.readlines()
	f.close();
	return lines;

def getFilePath(full_path):
	return os.path.dirname(full_path)
	
def dealPathSpace(_path):
	return os.popen(_path).read()

def getFileNameOfPath(full_path):
	return os.path.basename(full_path)
	
def getDirNameOfPath(full_path):
	return os.path.dirname(full_path)
	
def getFileCreateTime(_path):
	return os.path.getctime(_path)

def getFileModifyeTime(_path):
	return os.path.getmtime(_path)

def getFileSize(_path):
	return os.path.getsize(_path)
	
def getCrc32(_path):
	a_file = open(_path, 'rb')
	crc = binascii.crc32(a_file.read())
	a_file.close()
	return "%x"%(crc& 0xffffffff)

def getCrc32Files(files_list):
	crc_add = 0
	for _path in files_list:
		a_file = open(_path, 'rb')
		crc = binascii.crc32(a_file.read())
		a_file.close()
		crc_add += crc
	return "%x"%(crc_add& 0xffffffff)

#return True  if src_path is new than dst_path
def compareFile(src_path,dst_path):
	if not os.path.exists(dst_path):
		return True
	src_time =  getFileModifyeTime(src_path)
	dst_time =  getFileModifyeTime(dst_path)
	return src_time>dst_time
	
def backupFile(full_path):
	dst_file = full_path+_suffix
	shutil.copy(full_path,dst_file)
	
def revertFile(full_path):
	dst_file = full_path+_suffix
	if not os.path.exists(dst_file):
		log.logError("revert file: dst file not exist:"+dst_file)
		return
	shutil.copy(dst_file,full_path);
	
def checkPathForFile(path):
	_folder = os.path.dirname(path)
	if not os.path.exists(_folder):
		os.makedirs(_folder)

def safeCopy(srcFile,dstFile):
	if not os.path.exists(srcFile):
		log.printLog("file not exist:"+srcFile)
		return
	_folder = os.path.dirname(dstFile)
	if not os.path.exists(_folder):
		os.makedirs(_folder)
	shutil.copy(srcFile,dstFile)
	
def _copyFileOfDir(dir_from,dir_to,sub_dir,check_func):
	for name in os.listdir(sub_dir):
		_path = os.path.join(sub_dir, name)
		if os.path.isdir(_path):
			_copyFileOfDir(dir_from,dir_to,_path,check_func)
		else:
			_path_to = os.path.join(dir_to, _path[len(dir_from):])
			if check_func(_path_to):
				checkPathForFile(_path_to)
				shutil.copy(_path,_path_to)

def _createDirForCopy(path_from,path_to,sub_dir,check_func):
	if not check_func(sub_dir):
		log.printLog(sub_dir+"  ===> not create")
		return
	_to_sub_dir = os.path.join(path_to,sub_dir[len(path_from):])
	if not os.path.exists(_to_sub_dir):
		#log.printLog("makedirs:"+_to_sub_dir)
		os.makedirs(_to_sub_dir)
	for name in os.listdir(sub_dir):
		_path = os.path.join(sub_dir, name)
		if os.path.isdir(_path):
			_createDirForCopy(path_from,path_to,_path,check_func)

#拷贝文件夹下所有满足check_func的文件
def copyFolder(dir_from,dir_to,check_func):
	#create tree
	if not os.path.exists(dir_to):
		log.printLog("makedirs "+dir_to)
		os.makedirs(dir_to);

	for name in os.listdir(dir_from):
		_path = os.path.join(dir_from, name)
		if os.path.isdir(_path):
			_createDirForCopy(dir_from,dir_to,_path,check_func)

	#copy all files
	for name in os.listdir(dir_from):
		_path = os.path.join(dir_from, name)
		if os.path.isdir(_path):
			_copyFileOfDir(dir_from,dir_to,_path,check_func)
		else:
			_path_to = os.path.join(dir_to, name)
			if check_func(_path_to):
				shutil.copy(_path,_path_to)
				#log.printLog "copy file:"+_path_to
			#else:
				#log.printLog "file not copy:"+_path_to

def getFileSuffix(file):
	return os.path.splitext(file)[1]
	
def _pushFileOfDir(_dir,suffix,_list):
	for name in os.listdir(_dir):
		_path = os.path.join(_dir, name)
		if os.path.isdir(_path):
			_pushFileOfDir(_path,suffix,_list)
		elif not suffix is None:
			if getFileSuffix(_path)==suffix:
				_list.append(_path)
		else:
			_list.append(_path)
			
#获取所有给定后缀文件 suffix填None为不过滤
def getFileListOfDir(root_dir,suffix):
	_list = [];
	if not os.path.exists(root_dir):
		log.printLog("getFileListOfDir path not exits:"+root_dir)
		return _list
	_pushFileOfDir(root_dir,suffix,_list)
	return _list


	
if __name__ == "__main__":
	#_full_path = "D:/mobile/console/"
	log.printLog(getFileListOfDir("D:/mobile/console/",".py"))

