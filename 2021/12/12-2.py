# We are given an edge list
import fileinput

edges = []

for line in fileinput.input('12-input.txt'):
	edges.append(line[:-1].split('-'))

caves = {}

for edge in edges:
	for i in range(len(edge)):
		cave = edge[i]
		if cave not in caves:
			caves[cave] = [edge[1-i]]
		else:
			caves[cave].append(edge[1-i])

paths = {}

def find_path(node, visited, double, path):
	v = dict(visited)
	p = str(path)
	p += node
	if node == 'end':
		if p not in paths:
			print(len(paths))
			paths[p] = 0
		return
	if str.islower(node):
		if node in v:
			v[node] += 1
		else:
			v[node] = 1
	for adj in caves[node]:
		limit = 1
		if adj == double:
			limit = 2
		if (adj not in v or v[adj] < limit) and adj != 'start':
			if double == '' and str.islower(adj):
				find_path(adj, v, adj, p)
			find_path(adj, v, double, p)

find_path('start', {}, '', '')
print(len(paths))
