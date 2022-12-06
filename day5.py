import setup 
import re

def part1(text):
	pattern = re.compile(r"\d{1,5}")
	str_pattern = re.compile(r"[A-Z]")
	stacks, moves = text.split('\n\n')
	stacks = stacks.split('\n')
	new_stacks = []
	for i in range(0,len(stacks[-1]),4):
		new_stacks.append([str_pattern.findall(j[i:i+4]).pop() for j in stacks[:-1] if str_pattern.findall(j[i:i+4])])
	moves = moves.strip().split('\n')
	for move in moves:
		match = list(map(int,pattern.findall(move)))
		for i in range(match[0]):
			new_stacks[match[-1]-1].insert(0,new_stacks[match[1]-1].pop(0))

	return "".join([x[0] for x in new_stacks if x])

def part1TB():
	text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

	return part1(text)

def part2(text):
	pattern = re.compile(r"\d{1,5}")
	str_pattern = re.compile(r"[A-Z]")
	stacks, moves = text.split('\n\n')
	stacks = stacks.split('\n')
	new_stacks = []
	for i in range(0,len(stacks[-1]),4):
		new_stacks.append([str_pattern.findall(j[i:i+4]).pop() for j in stacks[:-1] if str_pattern.findall(j[i:i+4])])
	moves = moves.strip().split('\n')
	for move in moves:
		match = list(map(int,pattern.findall(move)))
		count = match[0]
		if count != 1:
			tmp = [new_stacks[match[1]-1].pop(0) for _ in range(count)]
			new_stacks[match[-1]-1] = tmp + new_stacks[match[-1]-1]
			# for i in range(count):
			# 	new_stacks[match[-1]-1].insert(0, tmp.pop(-1))
		else:
			new_stacks[match[-1]-1].insert(0,new_stacks[match[1]-1].pop(0))
	print(*new_stacks,sep="\n")

	return "".join([x[0] for x in new_stacks if x])

def part2TB():
	text = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

	return part2(text)

if __name__ == '__main__':
	file = setup.import_files(4)
	ans = part2TB()
	print(0)
	ans = part2(file[0])
	print(ans)

