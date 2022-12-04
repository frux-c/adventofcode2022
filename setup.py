import os

AOC_FILE_PATH = os.path.join(os.getcwd(),'AOC_INPUTS')

def import_files(index=None):
	rtn = []
	if index:
		assert index < len(os.listdir(AOC_FILE_PATH))
		with open(os.path.join(AOC_FILE_PATH,os.listdir(AOC_FILE_PATH)[index]),'r') as f:
			rtn.append(f.read().strip())
		return rtn
	for file in os.listdir(AOC_FILE_PATH):
		with open(os.path.join(AOC_FILE_PATH,file),'r') as f:
			rtn.append(f.read().strip())
	return rtn
