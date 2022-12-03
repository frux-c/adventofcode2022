import os

data = None
with open('AOC_input1.txt','r') as f:
	data = f.read().strip()
data = data.split('\n\n')
data = [sum(map(lambda x : float(x),dat.split('\n'))) for dat in data]
data = sorted(data,reverse=True)
print(len(data))
print(data[:5])
print(sum(data[:3]))