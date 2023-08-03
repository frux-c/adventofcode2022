from string import ascii_lowercase
import numpy as np 
import setup
import sys
import os
import copy

sys.setrecursionlimit(2 ** 31 - 1)
print(sys.getrecursionlimit())
kv = {ascii_lowercase[i] : i + 1 for i in range(len(ascii_lowercase))}
kv["S"] = 0
kv["E"] = 0

def find(arr,t):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i,j] == t : return (i,j)

def in_bound(arr,x,y):
	r,c = arr.shape
	return (0 <= x < r) and (0 <= y < c)

def in_rule(arr,x,y,x1,y1):
	return (arr[x,y] + 1) == arr[x1,y1] or (arr[x1,y1] <= arr[x,y])

def bfs(arr,start):
	# queue 
	Q = [(*start,0)]
	visited = set()
	row_move = [0,0,1,-1]
	col_move = [1,-1,0,0]
	pred = {start : None}
	while Q:
		# current idx
		x,y,step = Q.pop(0)
		if arr[x,y] == ord('E'):
			pred[start] = None
			return step,pred
		for tx,ty in zip(row_move,col_move):
			nx,ny = x + tx, y + ty
			if in_bound(arr, nx, ny):
				if arr[x,y] == ord('S'):
					Q.append((nx,ny,step+1))
					pred[(nx,ny)] = (x,y)
					visited.add((nx,ny))
				elif arr[x,y] == ord('z') and arr[nx,ny] == ord('E'):
					Q.append((nx,ny,step+1))
					pred[(nx,ny)] = (x,y)
					visited.add((nx,ny))
				elif in_rule(arr, x, y, nx, ny):
					if (nx,ny) not in visited:
						Q.append((nx,ny,step+1))
						pred[(nx,ny)] = (x,y)
					visited.add((nx,ny))

	return -1,{}

def getSteps(prev,end):
	jump = prev[end]
	steps = [end]
	while jump != None:
		jump = prev[jump]
		steps.insert(0, jump)
	return steps[1:]

def visualize(arr,steps):
	mat = np.array([
		[chr(l) for l in line] for line in arr])
	for row in mat:
		print(*row,sep=" ")
	for c,s in enumerate(steps[:len(steps)-1]):
		x,y = s
		nxt = steps[c+1]
		if s[0] > nxt[0]:
			mat[x,y] = '^'
		elif s[0] < nxt[0]:
			mat[x,y] = 'v'
		elif s[1] < nxt[1]:
			mat[x,y] = '>'
		else:
			mat[x,y] = '<'
	print()
	for row in mat:
		print(*row,sep=" ")

def part1(text):
	arr = np.array([[ord(j) for j in line] for line in text.strip().split('\n')])
	S = find(arr,ord('S'))
	E = find(arr,ord('E'))
	step,prev = bfs(arr,S)
	steps = getSteps(prev, E)
	visualize(arr, steps)
	print('exited code',step)


def part1TB():
	text = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
	part1(text)
	
# is literal
# == is therot


if __name__ == '__main__':
	file = setup.import_files("AOC_input12.txt")
	# part1TB()
	part1(file)