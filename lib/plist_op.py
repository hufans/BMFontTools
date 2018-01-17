import plistlib
import log


def readPlist(file_path):
	return plistlib.readPlist(file_path);
	
def searchPfDic(pf_dic,search_key,index):
	for key in pf_dic:
		if search_key == key:
			if isinstance(pf_dic[key],list):
				value =  pf_dic[key][index]
				return value
			else:
				return pf_dic[key]
	return ""
	
def getPlistValue(file_path,search_key,idx):
	pf = readPlist(file_path)
	return searchPfDic(pf,search_key,idx)
	

def searchPfDic_repace(pf_dic,search_key,replace_val,index):
	for key in pf_dic:
		if search_key == key:
			#log.printLog("find "+search_key+" : "+str(type(pf_dic[key])))
			if isinstance(pf_dic[key],list):
				log.printLog("replace list value:"+key+" index:"+str(index)+" with:"+str(replace_val))
				if index < len(pf_dic[key]):
					pf_dic[key][index] = replace_val
				else:
					pf_dic[key].append(replace_val)
			else:
				log.printLog("replace value:"+key+" with:"+str(replace_val))
				pf_dic[key] = replace_val
			return
		if isinstance(pf_dic[key],plistlib._InternalDict):
			searchPfDic_repace(pf_dic[key],search_key,replace_val,index)
		elif isinstance(pf_dic[key],list):
			searchPfList_repace(pf_dic[key],search_key,replace_val,index)

def searchPfList_repace(pf_list,search_key,replace_val,index):
	for val in pf_list:
		if isinstance(val,plistlib._InternalDict):
			searchPfDic_repace(val,search_key,replace_val,index)
		elif isinstance(val,list):
			searchPfList_repace(val,search_key,replace_val,index)

def replaceNormalValue(pfdata,key,val):
	searchPfDic_repace(pfdata,key,val,0)

def replaceListValue(pfdata,key,val,index):
	searchPfDic_repace(pfdata,key,val,index)

def writePlistFile(pf,file_path):
	plistlib.writePlist(pf,file_path)

if __name__ == "__main__":
	pf = readPlist("Info.plist")
	replaceNormalValue(pf,"CFBundleDisplayName","oooooooooo")
	writePlistFile(pf,"Info.plist")