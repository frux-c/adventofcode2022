import math 
import numpy as np
import setup

class Loc:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def jump(self,x,y):
		self.x = x
		self.y = y

	@property
	def position(self):
		return (self.x,self.y)

	def moveLeft(self,times=1):
		self.x -= times

	def moveRight(self,times=1):
		self.x += times

	def moveUp(self,times=1):
		self.y += times

	def moveDown(self,times=1):
		self.y -= times

	def __repr__(self):
		return f"{self.__class__.__name__}{self.__str__()}"

	def __str__(self):
		return f"({self.x},{self.y})"



def in_distance(H,T) -> None:
	dx = abs(T.x - H.x)
	dy = abs(T.y - H.y)
	tx,ty = 0,0
	if dx <= 1 and dy <= 1:
		return
	elif dx >= 2 and dy >= 2:
		tx = H.x-1 if T.x < H.x else H.x+1
		ty = H.y-1 if T.y < H.y else H.y+1
	elif dx >= 2:
		tx = H.x-1 if T.x < H.x else H.x+1
		ty = H.y
	elif dy >= 2:
		tx = H.x
		ty = H.y-1 if T.y < H.y else H.y+1
	T.jump(tx,ty)

def part1(text):
	pos_history = set()
	H = Loc()
	T = Loc()
	lst = text.strip().split('\n')
	for line in lst:
		d,m = line[0],int(line[2:])
		for _ in range(m):
			if d == 'U':
				H.moveUp()
			elif d == 'D':
				H.moveDown()
			elif d == 'L':
				H.moveLeft()
			elif d == 'R':
				H.moveRight()
			in_distance(H, T)
			pos_history.add(T.position)
	return H,T,len(pos_history)


def part1TB():
	text = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
	ans = part1(text)
	print(ans)
	return ans

def part2(text):
	pos_history = set()
	knots = [Loc() for _ in range(10)]
	lst = text.strip().split('\n')
	for line in lst:
		d,m = line[0],int(line[2:])
		for _ in range(m):
			if d == 'U':
				knots[0].moveUp()
			elif d == 'D':
				knots[0].moveDown()
			elif d == 'L':
				knots[0].moveLeft()
			elif d == 'R':
				knots[0].moveRight()
			for i in range(9):
				in_distance(knots[i], knots[i+1])
			pos_history.add(knots[-1].position)
	return knots[0],len(pos_history)
def part2TB():
	text = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
	ans = part2(text)
	print(ans)
if __name__ == '__main__':
	part1TB()
	file = setup.import_files(8)
	# ans = part1(file[0])
	# print(ans)
	part2TB()
	ans = part2(file[0])
	print(ans)
