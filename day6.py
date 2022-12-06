import setup

def part1(text):
	for i in range(len(text)-1):
		sset = set()
		for j in range(i+1,len(text)):
			if text[j] in sset: break
			sset.add(text[j])
			if len(sset) == 4:
				return j + 1
	return pos

def part1TB():
	text = [
		"mjqjpqmgbljsphdztnvjfqwrcgsmlb",
		"bvwbjplbgvbhsrlpgdmjqwftvncz",
		"nppdvjthqldpwncqszvftbrmjlhg",
		"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
		"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
	]
	ans = [7,5,6,10,11]
	for t,a in zip(text,ans):
		assert part1(t) == a
		print(f"Test Case \"{t}\" passed")

def part2(text):
	for i in range(len(text)-1):
		sset = set()
		for j in range(i+1,len(text)):
			if text[j] in sset: break
			sset.add(text[j])
			if len(sset) == 14:
				return j + 1
	return pos


def part2TB():
	text = [
		"mjqjpqmgbljsphdztnvjfqwrcgsmlb",
		"bvwbjplbgvbhsrlpgdmjqwftvncz",
		"nppdvjthqldpwncqszvftbrmjlhg",
		"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
		"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
	]
	ans = [19,23,23,29,26]
	for t,a in zip(text,ans):
		assert part2(t) == a
		print(f"Test Case \"{t}\" passed")


if __name__ == '__main__':
	file = setup.import_files(5)
	part1TB()
	ans = part1(file[0])
	print(ans)
	part2TB()
	ans = part2(file[0])
	print(ans)