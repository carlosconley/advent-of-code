import fileinput

moves = []

for line in fileinput.input("2-input.txt"):
	moves.append(line.split())


depth = 0
pos = 0

for move in moves:
	if move[0] == "down":
		depth += int(move[1])
	elif move[0] == "up":
		depth -= int(move[1])
	else:
		pos += int(move[1])

print(depth * pos)
