import fileinput
l = []
for line in fileinput.input("1-input.txt"):
	l.append(int(line))

prev = l[0]
counter = 0
for i in l[1:]:
	if i > prev:
		counter += 1
	prev = i

print(counter)