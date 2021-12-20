import fileinput

closing = [')', ']', '}', '>']
opening = ['(', '[', '{', '<']
scores = []
points = {'(':1, '[':2, '{':3, '<':4}

for line in fileinput.input('10-input.txt'):
	s = []
	skip = False
	for char in line:
		if len(s) == 0:
			if char in closing:
				skip = True
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
					skip = True
					break
			else:
				s.append(char)

	total = 0
	if not skip:
		while len(s) != 0:
			total = (total * 5) + points[s.pop()]
		scores.append(total)

print(sorted(scores)[len(scores) // 2])