from string import ascii_lowercase,ascii_uppercase
import setup

low_priority = {ascii_lowercase[l] : l + 1 for l in range(len(ascii_lowercase))}

high_priority = {ascii_uppercase[l] : l + 27 for l in range(len(ascii_uppercase))}

def part1(text):
	sim_sum = 0
	text = text.strip().split('\n')
	for line in text:
		m = len(line)//2
		s1,s2 = line[:m], line[m:]
		s1_set,s2_set = set(s for s in s1),set(s for s in s2)
		out = s1_set.intersection(s2_set)
		while out:
			l = out.pop()
			sim_sum += low_priority[l] if l in low_priority else high_priority[l]
	return sim_sum

def part2(text):
	sim_sum = 0
	text = text.strip().split('\n')
	assert len(text) % 3 == 0
	for i in range(0,len(text)-2,3):
		s1 = set(s for s in text[i])
		s2 = set(s for s in text[i+1])
		s3 = set(s for s in text[i+2])
		out = s1.intersection(s2).intersection(s3)
		while out:
			l = out.pop()
			sim_sum += low_priority[l] if l in low_priority else high_priority[l]
	return sim_sum


if __name__ == '__main__':
	txt = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
	files = setup.import_files()
	files = files[2]
	print(part2(files))

