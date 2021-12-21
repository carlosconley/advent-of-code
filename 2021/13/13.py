import fileinput

bottom = False
folds = []
points = set()

def print_paper(points, dim, line):
	paper = []

	for i in range(6):
		paper.append([' '] * 40)

	for point in points:
		paper[point[1]][point[0]] = '#'
	
	if dim > -1:
		for i in range(20):
			if dim == 0:
				paper[i][line] = '|'
			else:
				paper[line][i] = '-'

	for i in range(len(paper)):
		for char in paper[i]:
			print(char, end='')
		print()
	print()

for line in fileinput.input('13-input.txt'):
	if line == '\n':
		bottom = True
	elif bottom:
		folds.append(line.split()[-1].split('='))
	else:
		points.add(tuple([int(x) for x in line.split(',')]))

for fold in folds:
	new_points = set()
	line = int(fold[1])
	dim = int()
	if fold[0] == 'x':
		dim = 0
	else:
		dim = 1
	for point in points:
		if point[dim] > line:
			new_point = list(point)
			new_point[dim] = 2*line - point[dim]
			new_points.add(tuple(new_point))
		else:
			new_points.add(point)
	points = new_points

print_paper(points, -1, -1)
print(len(points))

