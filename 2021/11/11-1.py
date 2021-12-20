import fileinput, sys

octos = []
flashing = []
steps = 100
counter = 0

for line in fileinput.input('11-input.txt'):
	octos.append([int(x) for x in line if x.isdigit()])

width = len(octos)
height = len(octos[0])

for i in range(height):
	flashing.append([False] * width)

def flash(y, x):
	if 0 <= x < width and 0 <= y < height:
		octos[y][x] += 1
	else:
		return
	if octos[y][x] > 9 and not flashing[y][x]:
		flashing[y][x] = True
		global counter
		counter += 1
		up = y - 1
		left = x - 1
		down = y + 1
		right = x + 1

		flash(up, left)
		flash(up, x)
		flash(up, right)
		flash(y, left)
		flash(y, right)
		flash(down, left)
		flash(down, x)
		flash(down, right)

for i in range(steps):
	for y in range(len(octos)):
		for x in range(len(octos[y])):
			flash(y, x)

	for y in range(len(octos)):
		for x in range(len(octos[y])):
			if octos[y][x] > 9:
				octos[y][x] = 0
				flashing[y][x] = False
print(counter)
