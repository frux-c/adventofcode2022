import setup
import numpy as np
import ast
from functools import cmp_to_key
import sys

# sys.setrecursionlimit(3000)

def flatten(data):
	if len(data) == 0:
		return []
	lst = []

def parseData(_in):
	idx = 0
	out = []
	while idx < len(_in):
		if _in[idx].isnumeric():
			tmp = idx
			while _in[tmp].isnumeric():
				tmp += 1
			out.append(int(_in[idx:tmp]))
			idx = tmp
		else:
			idx += 1
	return out

# def checkOrder(left,right):
# 	if len(left) == 0:
# 		return True
# 	if len(right) == 0:
# 		return False
# 	if len(left) > len(right):
# 		return False
# 	for a,b in zip(left,right):
# 		if a > b: return False
# 	return True

def checkOrder(left,right):
	# print(type(left),type(right))
	if isinstance(left,int) and isinstance(right,int):
		if left == right: return None
		return left < right
	if isinstance(left,list) and isinstance(right,list):
		for a ,b in zip(left,right):
			x = checkOrder(a, b)
			if x is not None:
				return x
		return checkOrder(len(left),len(right))
	if isinstance(left,int):
		return checkOrder([left], right)
	return checkOrder(left, [right])

def convertOrder(left,right):
	# print(left,right)
	return -1 if checkOrder(left,right) else 1

def part1(text):
	_sum = 0
	for i, pair in enumerate(text.split('\n\n'),1):
		left, right = pair.split('\n')
		left = ast.literal_eval(left)
		right = ast.literal_eval(right)
		if checkOrder(left, right):
			_sum += i
			print(i)
	return _sum

# def findFirstNum(_in1,_in2):
# 	c1,c2 = 0,0
# 	while c1 < len(_in1) and c2 < len(_in2):
# 		n1,n2 = 0,0
# 		while c1 < len(_in1) and not _in1[c1].isnumeric():
# 			c1 += 1
# 		tmp = c1
# 		while c1 < len(_in1) and _in1[tmp].isnumeric():
# 			tmp += 1
# 		if _in1[c1:tmp].isnumeric():
# 			n1 = int(_in1[c1:tmp])
# 		while c2 < len(_in2) and not _in2[c2].isnumeric():
# 			c2 += 1
# 		tmp = c2
# 		while c2 < len(_in2) and _in2[tmp].isnumeric():
# 			tmp += 1
# 		if _in2[c2:tmp].isnumeric():
# 			n2 = int(_in2[c2:tmp])
# 		if n1 == n2:
# 			c1 += 1
# 			c2 += 1
# 			continue
# 		else:
# 			return -1 if n1 < n2 else 1
# 	return -1 if _in1.count('[') < _in2.count('[') else 1

def part2(text):
	arr = []
	for i, pair in enumerate(text.split('\n\n'),1):
		left, right = pair.split('\n')
		arr.append(ast.literal_eval(left))
		arr.append(ast.literal_eval(right))
		# arr.append(left)
		# arr.append(right)
	dv1 = [[2]]
	dv2 = [[6]]
	arr.append(dv1)
	arr.append(dv2)
	arr = sorted(arr,key=cmp_to_key(convertOrder))
	i = arr.index(dv1) + 1
	j = arr.index(dv2) + 1
	print(arr)
	return i * j

def part1TB():
	txt = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

	return part2(txt)

if __name__ == '__main__':
	file = setup.import_files("AOC_input13.txt")
	# ans = part1(file.strip())
	# ans = part1TB()
	ans = part2(file.strip())
	print(ans)