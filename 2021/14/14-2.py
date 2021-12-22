import fileinput
from math import log
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
			counts[char] = 0
	elif fileinput.lineno() > 2:
		rule = line.split(' -> ')
		rules[rule[0]] = {1:rule[1].strip()}
		for rule in rules:
			for char in rule:
				counts[char] = 0

for char in start:
	counts[char] += 1

def find_depth(length):
	if length < 2:
		return 1
	return log(length - 1, 2)

def polymerize(pair, depth):
	if depth == 0:
		return ''
	
	poly_depth = min(max(rules[pair]), depth)
	if poly_depth not in rules[pair]:
		poly_depth = 1

	poly = rules[pair][poly_depth]

	for char in poly:
		counts[char] += 1

	current = pair[0] + poly + pair[1]
	output = poly

	for i in range(len(current) - 1):
		if i < len(current) / 2
		output += polymerize(current[i] + current[i+1], depth - poly_depth)
	
	if output != '':
		rules[pair][depth] = output
	return output

for i in range(len(start) - 1):
	polymerize(start[i] + start[i+1], 2)

print(rules)
print(sum(counts.values()))
print(max(counts.values()) - min(counts.values()))