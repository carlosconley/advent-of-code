import fileinput

data = []
for line in fileinput.input('3-input.txt'):
	data.append(list(line)[:-1])

common = []
for i in range(len(data[0])):
	common.append(0)

for bits in data:
	for i in range(len(bits)):
		common[i] += int(bits[i])

i = 0
gamma = 0
epsilon = 0

for val in reversed(common):
	if val >= 500:
			gamma += 1 * 2**i
			epsilon += 0 * 2**i
	else:
		gamma += 0 * 2**i
		epsilon += 1 * 2**i

	i += 1

print(gamma * epsilon)
