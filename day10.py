import setup

def part1(text):
	intercept = {20,60,100,140,180,220}
	cycle_count = 0
	_sum = 0
	reg = 1
	lines = text.split('\n')
	idx = 0
	in_cycle = False
	queue = []
	while idx < len(lines):
		if cycle_count in intercept:
			_sum += (cycle_count * reg)

		if in_cycle:
			if cycle_count == offset:
				in_cycle = False
				reg += queue.pop(0)
			else:
				cycle_count += 1
				continue

		tmp = lines[idx].split(' ')
		if len(tmp) == 1:
			tmp.append(None)
		cmd, arg = tmp
		if cmd == 'addx':
			in_cycle = True
			offset = cycle_count + 2
			queue.append(int(arg))
		cycle_count += 1
		idx += 1
	if queue:
		reg += queue.pop(0)
	print(cycle_count)
	print(reg)
	print(_sum)
	"""
	for line in lines:
		args = line.split(' ')
		if args[0] == 'noop':
			cycle_count += 1
			if cycle_count in intercept:
				_sum += cycle_count * reg
		elif args[0] == 'addx':
			cycle_count += 1
			if cycle_count in intercept:
				_sum += cycle_count * reg
			cycle_count += 1
			if cycle_count in intercept:
				_sum += cycle_count * reg
			reg = int(args[1])
	print(reg)
	"""
def part1TB():
	part1(text)

def part2(text):
	intercept = 0
	cycle_count = 0
	reg = 1
	lines = text.strip().split('\n')
	idx = 0
	in_cycle = False
	queue = []
	while idx < len(lines):
		if intercept == 40:
			intercept = 0
			print()
		if abs(reg - intercept + 1) <= 1:
			print("|",end="")
		else:
			print(" ",end="")
		if in_cycle:
			if cycle_count == offset:
				in_cycle = False
				reg += queue.pop(0)
			else:
				cycle_count += 1
				intercept += 1
				continue

		tmp = lines[idx].split(' ')
		if len(tmp) == 1:
			tmp.append(None)
		cmd, arg = tmp
		if cmd == 'addx':
			in_cycle = True
			offset = cycle_count + 2
			queue.append(int(arg))
		cycle_count += 1
		idx += 1
		intercept += 1
	if queue:
		reg += queue.pop(0)
	print()
	print(cycle_count)
	print(reg)


if __name__ == '__main__':
	# file = setup.import_files('AOC_input10TB.txt')
	file = setup.import_files('AOC_input10.txt')
	part1(file[0])
	part2(file[0])
