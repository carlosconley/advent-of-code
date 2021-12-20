import fileinput

dim = 1000
points = [([0] * dim) for row in range(dim)]

paths = []
for line in fileinput.input('5-input.txt'):
	coords = [[int(l) for l in k] for k in [j.split(',') for j in [i for i in line.split('->')]]]
	paths.append(coords)	

for path in paths:
	x1,y1 = path[0][0], path[0][1]
	x2,y2 = path[1][0], path[1][1]

	while True:
		points[y1][x1] += 1
		if x1 == x2 and y1 == y2:
			break
		if x1 < x2:
			x1 += 1
		elif x1 > x2:
			x1 -= 1
		
		if y1 < y2:
			y1 += 1
		elif y1 > y2:
			y1 -= 1

count = 0
for row in points:
	for point in row:
		if point > 1:
			count += 1

print(count)
