import fileinput
from math import log
''' Create dict of polymer rules {pair -> insertion}
	Create dict of polymer count {polymer -> count}
	Shouldn't need to keep track of polymer
	Complete with recursion, each interaction should create two more until depth of 5 is reached

'''

rules = {}
counts = {}
c_counts = {}
start = str()

for line in fileinput.input('14-input.txt'):
	if fileinput.lineno() == 1:
		start = line[:-1]

	elif fileinput.lineno() > 2:
		rule = line.split(' -> ')
		rules[rule[0]] = rule[1].strip()

for rule in rules:
	counts[rule] = 0

for i in range(len(start) - 1):
	counts[start[i:i+2]] += 1

def freq(pairs):
	new_pairs = dict(pairs)
	for pair in pairs:
		count = counts[pair]
		new_pairs[pair] -= count
		new_pairs[pair[0] + rules[pair]] += count
		new_pairs[rules[pair] + pair[1]] += count

	return new_pairs



for i in range(40):
	counts = freq(counts)

for pair in counts:
	for char in pair:
		if char not in c_counts:
			c_counts[char] = 0
		c_counts[char] += counts[pair]

c_counts[start[0]] += 1
c_counts[start[-1]] += 1

for char in c_counts:
	c_counts[char] //= 2

print(c_counts)
print(max(c_counts.values()) - min(c_counts.values()))