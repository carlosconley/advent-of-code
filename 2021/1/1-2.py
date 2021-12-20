import fileinput
l = []
for line in fileinput.input("1-input.txt"):
	l.append(int(line))

prev = sum(l[0:3])
counter = 0

for i in range(len(l) - 3):
	current = prev - l[i] + l[i+3]
	if current > prev:
		counter += 1
	prev = current

print(counter)
	