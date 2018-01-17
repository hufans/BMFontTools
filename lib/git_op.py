import os
import sys
import shutil
import log
import syscmd

ori_work_dir = os.getcwd()
local_path = os.path.dirname(__file__)
git_root_dit = local_path+"/../../"


def checkout_commit(commit):
	os.chdir(git_root_dit)
	log.stash_log(True)
	log.printLog( syscmd.exec_cmd("git reset --hard HEAD") )
	log.printLog( syscmd.exec_cmd("git clean -dfx") )
	log.printLog( syscmd.exec_cmd("git fetch origin") )
	log.printLog( syscmd.exec_cmd("git checkout "+commit) )
	#syscmd.exec_cmd("git reset --hard HEAD")
	log.stash_log(False)
	os.chdir(ori_work_dir)
	
def get_cur_commit_id():
	result = syscmd.exec_cmd("git rev-parse HEAD")
	if result[len(result)-1:] =="\n":
		result = result[0:len(result)-1]
	return result

def find_in_list(val,list):
	for _v in list:
		if _v == val:
			return True
	return False

def diff_change_list(commit_cur,commit_prev):
	result = syscmd.exec_cmd("git diff --name-only "+commit_cur+" "+commit_prev)
	if result[len(result)-1:] =="\n":
		result = result[0:len(result)-1]
	lines1 = result.split('\n')
	
	result = syscmd.exec_cmd("git diff --name-only "+commit_prev+" "+commit_cur)
	if result[len(result)-1:] =="\n":
		result = result[0:len(result)-1]
	lines2 = result.split('\n')
	
	lines = lines1[:]
	for _line in lines2:
		if not find_in_list(_line,lines1):
			lines.append(_line)
	
	return lines

if __name__ == "__main__":
	#checkout_commit("test_tag")
	#id = get_cur_commit_id()
	diff_change_list("564817f85cd82558579c665ad923521f44000186","2040ac5ad408d3afc6404dcd4110b13f46083b0f")