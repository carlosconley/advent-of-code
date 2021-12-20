import fileinput

data = []
for line in fileinput.input('3-input.txt'):
	data.append(list(line)[:-1])


nums = data
index = 0
while len(nums) > 1:
	c_nums = []
	ones = 0
	for num in nums:
		ones += int(num[index])
	zeros = len(nums) - ones
	if ones >= zeros:
		common = '1'
	else:
		common = '0'
	print(common, index)
	for num in nums: 
		if num[index] == common:
			c_nums.append(num)
			print(num)
	nums = c_nums
	index += 1

oxygen = 0
i = 0
for bit in reversed(nums[0]):
	oxygen += int(bit) * 2**i
	i += 1

print(nums, oxygen)
nums = data
index = 0
while len(nums) > 1:
	l_nums = []
	ones = 0
	for num in nums:
		ones += int(num[index])
	zeros = len(nums) - ones
	if ones >= zeros:
		least = '0'
	else:
		least = '1'
	for num in nums: 
		if num[index] == least:
			l_nums.append(num)
	nums = l_nums
	index += 1

carbon = 0
i = 0
for bit in reversed(nums[0]):
	carbon += int(bit) * 2**i
	i += 1

print(nums, carbon)

print(oxygen * carbon)