import setup

def outcome(a,b):
	if a == b:
		return 3
	if a == 'A':
		return [0,6][b == 'B']
	if a == 'B':
		return [0,6][b == 'C']
	if a == 'C':
		return [0,6][b == 'A']


def final_score(game):
	p = {
		'A' : 1,
		'B' : 2,
		'C' : 3,
	}
	c = {
		'X' : 'A',
		'Y' : 'B',
		'Z' : 'C',
	}
	game = game.strip()
	game = game.split('\n')
	points = 0
	for r in game:
		p1,p2 = r[0],c[r[-1]]
		if p2 == 'A':
			points += (p[p1] - 1) if p1 != 'A' else 3
		elif p2 == 'B':
			points += p[p1] + 3
		elif p2 == 'C':
			points += 6 + ((p[p1] + 1) if p1 != 'C' else 1)
	return points

if __name__ == '__main__':
	files = setup.import_files()
	files = files[1]
	txt = """A Y\nB X\nC Z"""
	print(final_score(files))
