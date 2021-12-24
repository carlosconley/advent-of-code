import fileinput
from collections import deque
from typing import Tuple, Set

risks = []

for line in fileinput.input('15-input.txt'):
	risks.append([int(x) for x in line.strip()])

height = len(risks)
width = len(risks[0])
start, end = (0, 0), (width - 1, height - 1)
dist = {}
prev = {}
max_risk = 0

for risk in risks:
	max_risk += sum(risk)


def get_neighbors(t: Tuple) -> Set[Tuple]:
	x = t[0]
	y = t[1]
	n = set()

	if x > 0:
		n.add((x-1, y))
	if y > 0:
		n.add((x, y-1))
	if x < width - 1:
		n.add((x+1, y))
	if y < height - 1:
		n.add((x, y+1))

	return n


nodes = set()

for y in range(height):
	for x in range(width):
		dist[(x,y)] = max_risk
		prev[(x,y)] = None
		nodes.add((x,y))

dist[start] = 0

while len(nodes) > 0:
	current = min(nodes, key=lambda x: dist[x])
	nodes.remove(current)

	if current == end:
		break

	for neighbor in get_neighbors(current):
		alt = dist[current] + risks[neighbor[1]][neighbor[0]]
		if alt < dist[neighbor]:
			dist[neighbor] = alt
			prev[neighbor] = current

s = []
current = end



if prev[current] is not None:
	while current is not None:
		s.insert(0, current)
		current = prev[current]

print(sum(risks[x[1]][x[0]] for x in s) - risks[0][0])