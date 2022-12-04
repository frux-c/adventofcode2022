import setup

def part1(text):
	text_list = text.split('\n')
	text_list = [line.split(',') for line in text_list]
	text_list = [[tuple(map(int,s1.split('-'))),tuple(map(int,s2.split('-')))] for s1,s2 in text_list]
	count = 0
	for line in text_list:
		t1,t2 = line
		a,a1 = t1
		b,b1 = t2
		if a <= b <= a1 and a <= b1 <= a1:
			count += 1
		elif b <= a <= b1 and b <= a1 <= b1:
			count += 1
	return count

def part1TB():
	text = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
	assert part1(text.strip()) == 2

def part2(text):
	text_list = text.split('\n')
	text_list = [line.split(',') for line in text_list]
	text_list = [[tuple(map(int,s1.split('-'))),tuple(map(int,s2.split('-')))] for s1,s2 in text_list]
	count = 0
	for line in text_list:
		t1,t2 = line
		a,a1 = t1
		b,b1 = t2
		if a <= b <= a1 or a <= b1 <= a1:
			count += 1
		elif b <= a <= b1 or b <= a1 <= b1:
			count += 1
	return count

def part2TB():
	text = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
	assert part2(text.strip()) == 4
if __name__ == '__main__':
	part1TB() # test case
	print("part1 test case passed")
	part2TB()
	print("part2 test case passed")
	file = setup.import_files(3)
	A = part1(file[0])
	print(A)
	B = part2(file[0])
	print(B)