import fileinput

outputs, patterns = [], []
for line in fileinput.input('8-input.txt'):
	patterns.append([x for x in line.split(' | ')][0].split())
	outputs.append([x for x in line.split(' | ')][1].split())

u_lens = {2:1, 7:8, 4:4, 3:7}
output = 0

def sub(str1, str2):
	output = str1
	for letter in str2:
		if letter in output:
			output = output.replace(letter, '')
	return output

def contains(str1, str2):
	for letter in str2:
		if letter not in str1:
			return False
	return True

number = 0

for i in range(len(patterns)):
	size = 0
	pattern_map = [''] * 10
	letter_map = {}
	while size < 10:
		for pattern in patterns[i]:
			p = str().join(sorted(pattern))
			if size < 4:
				if len(p) in u_lens:
					pattern_map[u_lens[len(p)]] = p
					size += 1
			elif size < 7:
				if len(p) == 5:
					if contains(p, pattern_map[7]):
						pattern_map[3] = p
						size += 1
					elif contains(p, sub(pattern_map[4], pattern_map[1])):
						pattern_map[5] = p
						size += 1
					else:
						pattern_map[2] = p
						size += 1
			else:
				if pattern_map[0] == '':
					d = sub(sub(pattern_map[4], pattern_map[1]), sub(pattern_map[8], pattern_map[3]))
					pattern_map[0] = sub(pattern_map[8], d)
					size += 1
				if pattern_map[9] == '':
					e = sub(pattern_map[2], pattern_map[3])
					pattern_map[9] = sub(pattern_map[8], e)
					size += 1
				if pattern_map[6] == '':
					c = sub(pattern_map[7], pattern_map[5])
					pattern_map[6] = sub(pattern_map[8], c)	
					size += 1	
	
	digit_letters = ''
	for output in outputs[i]:
		o = str().join(sorted(output))
		digit_letters += str(pattern_map.index(o))
	number += int(digit_letters)

print(number)


