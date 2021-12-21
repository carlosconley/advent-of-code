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

counter = 0

def find_path(node, visited):
	l = list(visited)
	if node == 'end':
		global counter
		counter += 1
		return

	if str.islower(node):
		l.append(node)
	for adj in caves[node]:
		if adj not in l:
			find_path(adj, l)

find_path('start', [])

print(counter)