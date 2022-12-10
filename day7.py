import setup
import numpy as np

class File:
	def __init__(self,name : str,size : int) -> None:
		self.name = name
		self.size = size

	def __repr__(self):
		return f"{self.__class__.__name__}({self.name},{self.size})"

	def __str__(self):
		return self.name

class Dir:
	def __init__(self, name, parent=None):
		self.name = name
		self.dirs = []
		self.files = []
		self.parent = parent

	def getDir(self,_dir):
		for tdir in self.dirs:
			if tdir.name == _dir:
				return tdir
		return None 

	def __repr__(self):
		return self.name

# def parseCommand(root,command):


def part1(text):
	root = Dir("/")
	trav = root
	lst = text.strip().split('\n')
	mx = 0
	while mx < len(lst):
		line = lst[mx]
		if line[0] == '$': # its a command
			line_split = line[2:].split(' ')
			if len(line_split) == 1:
				line_split.append(None)
			cmd, arg = line_split

			if cmd == 'cd': # if change directory
				if arg == '/': # move eto root
					trav = root
				elif arg == '..': # move back to parent
					if trav.parent:
						trav = trav.parent
				else: # move into a directory
					_dir = trav.getDir(arg)
					if _dir:
						trav = _dir

			elif cmd == 'ls': # if list directory
				mx += 1
				while mx < len(lst) and lst[mx][0] != '$': # look ahead
					tp,dr = lst[mx].split(' ')
					if tp == 'dir':
						# print('adding file')
						new_dir = Dir(name=dr,parent=trav)
						trav.dirs.append(new_dir)
					else:
						tp = int(tp)
						new_file = File(name=dr,size=tp)
						trav.files.append(new_file)
					mx += 1
				mx -= 1
		mx += 1
	return root

def sumDirFiles(_dir):
	if _dir == None:
		return 0
	s = sum([x.size for x in _dir.files])
	for d in _dir.dirs:
		s += sumDirFiles(d)
	return s

def sumDirUnderHThousand(_dir):
	s = sumDirFiles(_dir)
	if s > 100_000:
		s = 0
	for d in _dir.dirs:
		s += sumDirUnderHThousand(d)
	return s

def f_min(a,b):
	if a[1] < b[1]:
		return a
	return b

def dir_stats(_dir,rmd,req):
	size = sumDirFiles(_dir)
	free = req - (rmd + size)
	free = np.inf if free > 0 else abs(free)
	m = [(_dir,size,free)]
	for d in _dir.dirs:
		m += dir_stats(d, rmd, req)
	return m

def f_min2(lst):
	_min = None,np.inf,np.inf
	for d in lst:
		if d[2] < _min[2]:
			_min = d
	return _min

def part2(text):
	root = part1(text)
	max_size = 70_000_000
	csize = sumDirFiles(root)
	rmd = max_size - csize
	req = 30_000_000
	data = dir_stats(root, rmd, req)
	print(f_min2(data))

def part1TB():
	text= """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
	return part1Ext(text)

def part2TB():
	text= """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
	part2(text)

if __name__ == '__main__':
	file = setup.import_files(6)
	part1TB()
	ans = part1(file[0])
	print(sumDirUnderHThousand(ans))
	part2TB()
	ans = part2(file[0])
