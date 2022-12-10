import setup
import numpy as np 

def part1(text):
	arr = np.array(
		[[n for n in line] 
		for line in text.strip().split('\n')]
		,dtype=np.int8)
	count = (2 * len(arr)) + (2 * len(arr[0])) - 4
	# print(count)
	for i in range(1,len(arr)-1):
		for j in range(1,len(arr[i])-1):
			# print(arr[:i,j])
			_min = min(
				max(arr[:i,j]), # to top
				max(arr[i+1:,j]), # to bottom,
				max(arr[i,:j]), # to left
				max(arr[i,j+1:])) # to right
			if arr[i,j] > _min:
				count += 1
	return count



def part1TB():
	text = """30373
25512
65332
33549
35390
	"""
	print(part1(text))


def get_score(arr,i,j):
	top = 0
	for n in arr[:i,j][::-1]:
		top += 1
		if arr[i,j] <= n:
			break
	bottom = 0
	for n in arr[i+1:,j]:
		bottom += 1
		if arr[i,j] <= n:
			break

	left = 0
	for n in arr[i,:j][::-1]:
		left += 1
		if arr[i,j] <= n:
			break

	right = 0
	for n in arr[i,j+1:]:
		right += 1
		if arr[i,j] <= n:
			break
			
	return top * bottom * left * right


def part2(text):
	arr = np.array(
		[[n for n in line] 
		for line in text.strip().split('\n')]
		,dtype=np.int8)
	# print(arr)
	r = len(arr) - 1
	c = len(arr[0]) - 1
	_max = 0
	for i in range(1,r):
		for j in range(1,c):
			_max = max(_max, get_score(arr, i, j))
	return _max

def part2TB():
	text = """30373
25512
65332
33549
35390
	"""
	print(part2(text))

if __name__ == '__main__':
	file = setup.import_files(7)
	# part1TB()
	ans = part1(file[0])	
	print(ans)
	# part2TB()
	ans = part2(file[0])
	print(ans)