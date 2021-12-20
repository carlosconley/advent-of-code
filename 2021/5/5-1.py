import fileinput

dim = 1000
points = [([0] * dim) for row in range(dim)]

paths = []
for line in fileinput.input('5-input.txt'):
	coords = [[int(l) for l in k] for k in [j.split(',') for j in [i for i in line.split('->')]]]
	if coords[0][0] == coords[1][0] or coords[0][1] == coords[1][1]:
		paths.append(coords)	

for path in paths:
	print(path)
	height = None
	width = None

	if path[0][0] < path[1][0]:
		height = range(path[0][0], path[1][0] + 1)
	else:
		height = range(path[1][0], path[0][0] + 1)
	
	if path[0][1] < path[1][1]:
		width = range(path[0][1], path[1][1] + 1)
	else:
		width = range(path[1][1], path[0][1] + 1)

	for y in height:
		for x in width:
			points[y][x] += 1

count = 0
for row in points:
	for point in row:
		if point > 1:
			count += 1

print(count)
