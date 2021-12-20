import fileinput

hmap = []

for line in fileinput.input('9-input.txt'):
	hmap.append([int(x) for x in line if str.isdigit(x)])

length = len(hmap)
width = len(hmap[0])
low_points = []

for y in range(length):
	for x in range(width):
		h = hmap[y][x]

		if y - 1 >= 0 and hmap[y-1][x] <= h:
			continue
		elif x - 1 >= 0 and hmap[y][x-1] <= h:
			continue
		elif y + 1 < length and hmap[y+1][x] <= h:
			continue
		elif x + 1 < width and hmap[y][x+1] <= h:
			continue
		else:
			low_points.append((x, y))

visited = []
for i in range(length):
	visited.append([False] * width)

# dfs starting at a given point, ending when we hit a 9
# each time we traverse to a new point, we increase basin size

depths = []
for point in low_points:
	s = []
	current = point
	finished = False
	size = 0
	while not finished:
		size += 1
		x, y = current[0], current[1]
		visited[y][x] = True
		
		if y - 1 >= 0 and not visited[y-1][x] and hmap[y-1][x] < 9:
			s.insert(0, (x, y - 1))
		if x - 1 >= 0 and not visited[y][x-1] and hmap[y][x-1] < 9:
			s.insert(0, (x - 1, y))
		if y + 1 < length and not visited[y+1][x] and hmap[y+1][x] < 9:
			s.insert(0, (x, y + 1))
		if x + 1 < width and not visited[y][x+1] and hmap[y][x+1] < 9:
			s.insert(0, (x + 1, y))
		
		
		while len(s) > 0 and visited[current[1]][current[0]]:
			current = s.pop()

		if len(s) == 0 and visited[current[1]][current[0]]:
			finished = True

	depths.append(size)
		
prod = 1
for size in sorted(depths)[-3:]:
	prod *= size
print(prod)