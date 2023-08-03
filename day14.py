import numpy as np
import setup
import re

class Sand:
	def __init__(self,x,y):
		self.px = x
		self.py = y
		self.x = x
		self.y = y
		self.rest = False
	
	def fall(self, grid):
		if grid.grid[self.x + 1, self.y] == 0:
			self.x += 1
		elif grid.grid[self.x + 1, self.y - 1] == 0:
			self.x += 1
			self.y -= 1
		elif grid.grid[self.x + 1, self.y + 1] == 0:
			self.x += 1
			self.y += 1
		else:
			grid.grid[self.x, self.y] = 2
			self.rest = True

	def reset(self):
		self.x = self.px
		self.y = self.py
		self.rest = False

class Grid:
	def __init__(self, n, m):
		self.grid = np.zeros((n,m), dtype=int)
		self.count = 0

	def add_rock(self, x, y):
		print('adding rock at',x,y)
		try:
			self.grid[x, y] = 1
		except IndexError:
			return

	def pour_sand(self, x , y):
		sand = Sand(x ,y)
		while True:
			try:
				while sand.fall(self.grid):
					continue
				self.count += 1
			except IndexError:
				break
	def __str__(self):
		return self.grid.__str__()

def get_int_paths(rock_path):
	paths = rock_path.split("->")
	xy_path = []
	for path in paths:
		x, y= path.strip().split(",")
		xy_path.append((int(y), int(x)))
	return xy_path

def parse_data(input_data):
	rock_paths = input_data.strip().split("\n")
	new_paths = list(map(get_int_paths, rock_paths))
	return new_paths

def part1(input_data):
	rocks = parse_data(input_data)
	v = np.iinfo(np.int32)
	x_min, x_max, y_min, y_max = v.max, v.min, v.max, v.min
	for paths in rocks:
		for path in paths:
			x, y = path
			if x < x_min:
				x_min = x
			if x > x_max:
				x_max = x
			if y < y_min:
				y_min = y
			if y > y_max:
				y_max = y
	print(x_min, x_max, y_min, y_max)

	dx = (x_max - x_min) + 1
	dy = (y_max - y_min) + 1
	grid = Grid(dx, dy)
	for paths in rocks:
		for i, path in enumerate(paths[1:]):
			tx, ty = paths[i][0] - x_min, paths[i][1] - y_min
			tdx, tdy = (path[0] - paths[i][0]), (path[1] - paths[i][1])
			# ofx, ofy = (x_max - paths[i][0]), (y_max - paths[i][1])
			print(f"{paths[i][0]}, {paths[i][1]} -> {path[0]}, {path[1]}")
			print(tx - 1, ty - 1)
			# grid.add_rock(tx, ty)
			# print('offsets', ofx, ofy)
			# # print(tdx, tdy)
			if tdx:
			# 	print('tdx', tdx)
				if tdx > 0:
					for j in range(tdx):
						grid.add_rock(tx + j, ty)
				else:
					for j in range(tdx, 1, -1):
						grid.add_rock(tx + j, ty)
			if tdy:
				if tdy > 0:
					for j in range(tdy):
						grid.add_rock(tx, ty + j)
				else:
					for j in range(tdy, 1, -1):
						grid.add_rock(tx, ty + j)
		print()
	print(grid)


if __name__ == "__main__":
	# data = setup.import_files("AOC_input14.txt")
	data = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
	"""
	part1(data)
