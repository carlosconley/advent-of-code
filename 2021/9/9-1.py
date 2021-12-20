import fileinput

hmap = []

for line in fileinput.input('9-input.txt'):
	hmap.append([int(x) for x in line if str.isdigit(x)])

length = len(hmap)
width = len(hmap[0])
total = 0

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
			total += h + 1

print(total)
