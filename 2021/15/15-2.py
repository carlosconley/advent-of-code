import fileinput, heapq
from typing import Tuple, Set

risks_small = []

def scale(x:int, i:int) -> int:
	x += i
	if x > 9:
		x = x - 9
	return x


for line in fileinput.input('15-input.txt'):
	row = [int(x) for x in line.strip()]
	risks_small.append(list(row))
	for i in range(1, 5):
		risks_small[-1] = risks_small[-1] + [(x - 1 + i) % 9 + 1 for x in row]

risks = []

for i in range(0, 5):
	for row in risks_small:
		risks.append([(x - 1 + i) % 9 + 1 for x in row])


height = len(risks)
width = len(risks[0])
start, end = (0, 0), (width - 1, height - 1)



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

# Use heap for runtime efficiency
heap = [(0, 0, 0)]
path_risk = {}
visited = set()

while len(heap) > 0:
	c, x, y = heapq.heappop(heap)

	if (x, y) in visited:
		continue
	visited.add((x, y))

	path_risk[(x, y)] = c

	if (x, y) == end:
		break

	for neighbor in get_neighbors((x, y)):
		heapq.heappush(heap, (c + risks[neighbor[1]][neighbor[0]], neighbor[0], neighbor[1]))

print(path_risk[end])