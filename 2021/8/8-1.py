import fileinput

output, patterns = [], []
for line in fileinput.input('8-input.txt'):
	patterns.append([x for x in line.split(' | ')][0].split())
	output.append([x for x in line.split(' | ')][1].split())

count = {1:0, 4:0, 7:0, 8:0}
u_lens = {2:1, 7:8, 4:4, 3:7}

for digits in output:
	for digit in digits:
		if len(digit) in u_lens:
			count[u_lens[len(digit)]] += 1

print(sum(count.values()))
