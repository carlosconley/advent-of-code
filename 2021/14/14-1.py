import fileinput
''' Create dict of polymer rules {pair -> insertion}
	Create dict of polymer count {polymer -> count}
	Shouldn't need to keep track of polymer
	Complete with recursion, each interaction should create two more until depth of 5 is reached

'''

rules = {}
counts = {}
start = str()

for line in fileinput.input('14-input.txt'):
	if fileinput.lineno() == 1:
		start = line[:-1]
		for char in line[:-1]:
			if char not in counts:
				counts[char] = 0
			counts[char] += 1
	elif fileinput.lineno() > 2:
		rule = line.split(' -> ')
		rules[rule[0]] = rule[1].strip()

def polymerize(pair, depth):
	if depth == 0:
		return
	poly = rules[pair]
	if poly not in counts:
		counts[poly] = 0
	counts[poly] += 1

	polymerize(pair[0] + poly, depth - 1)
	polymerize(poly + pair[1], depth - 1)

for i in range(len(start) - 1):
	polymerize(start[i] + start[i+1], 10)



print(max(counts.values()) - min(counts.values()))