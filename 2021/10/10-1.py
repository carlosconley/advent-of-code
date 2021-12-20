import fileinput

closing = [')', ']', '}', '>']
opening = ['(', '[', '{', '<']
values = {')':3, ']':57, '}':1197, '>':25137}
corrupted = []

for line in fileinput.input('10-input.txt'):
	s = []
	for char in line:
		if len(s) == 0:
			if char in closing:
				corrupted.append(char)
				break
			else:
				s.append(char)
		else:
			if char == '\n':
				continue
			if char in closing:
				i = closing.index(char)
				if s[-1] == opening[i]:
					s.pop()
				else:
					corrupted.append(char)
					break
			else:
				s.append(char)

points = 0
for char in corrupted:
	points += values[char]

print(points)