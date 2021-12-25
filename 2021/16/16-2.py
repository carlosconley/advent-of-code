import fileinput, math

decimal = int('E0525D9802FA00B80021B13E2D4260004321DC648D729DD67B2412009966D76C0159ED274F6921402E9FD4AC1B0F652CD339D7B82240083C9A54E819802B369DC0082CF90CF9280081727DAF41E6A5C1B9B8E41A4F31A4EF67E2009834015986F9ABE41E7D6080213931CB004270DE5DD4C010E00D50401B8A708E3F80021F0BE0A43D9E460007E62ACEE7F9FB4491BC2260090A573A876B1BC4D679BA7A642401434937C911CD984910490CCFC27CC7EE686009CFC57EC0149CEFE4D135A0C200C0F401298BCF265377F79C279F540279ACCE5A820CB044B62299291C0198025401AA00021D1822BC5C100763A4698FB350E6184C00A9820200FAF00244998F67D59998F67D5A93ECB0D6E0164D709A47F5AEB6612D1B1AC788846008780252555097F51F263A1CA00C4D0946B92669EE47315060081206C96208B0B2610E7B389737F3E2006D66C1A1D4ABEC3E1003A3B0805D337C2F4FA5CD83CE7DA67A304E9BEEF32DCEF08A400020B1967FC2660084BC77BAC3F847B004E6CA26CA140095003900BAA3002140087003D40080022E8C00870039400E1002D400F10038C00D100218038F400B6100229500226699FEB9F9B098021A00800021507627C321006E24C5784B160C014A0054A64E64BB5459DE821803324093AEB3254600B4BF75C50D0046562F72B1793004667B6E78EFC0139FD534733409232D7742E402850803F1FA3143D00042226C4A8B800084C528FD1527E98D5EB45C6003FE7F7FCBA000A1E600FC5A8311F08010983F0BA0890021F1B61CC4620140EC010100762DC4C8720008641E89F0866259AF460C015D00564F71ED2935993A539C0F9AA6B0786008D80233514594F43CDD31F585005A25C3430047401194EA649E87E0CA801D320D2971C95CAA380393AF131F94F9E0499A775460', 16)

binary = str(bin(decimal))[2:]

meta_len = 3
lit_len = 5

version_sum = 0

while len(binary) % 8 != 0:
	binary = '0' + binary

index = 0
# returns the value of the literal
def parse_literal(binary: str) -> int:
	global index
	s_literal = binary[index + 1: index + lit_len]
	i = lit_len + index
	while binary[i - lit_len] != '0':
		s_literal += binary[i+1:i+lit_len]
		i += lit_len
	index = i
	return int(s_literal, 2)

# returns the value of the operator
def parse_operator(binary: str, t: int) -> int:
	global index
	l = binary[index]
	index += 1
	packets = []
	if  l == '0':
		packet_len = int(binary[index:index+15], 2) + index + 15
		index += 15
		while index < packet_len:
			packets.append(parse_packet(binary))

	elif l == '1':
		sub_packets = int(binary[index:index+11], 2)
		index += 11
		for i in range(sub_packets):
			packets.append(parse_packet(binary))

	if t == 0:
		return sum(packets)
	elif t == 1:
		return math.prod(packets)
	elif t == 2:
		return min(packets)
	elif t == 3:
		return max(packets)
	elif t == 5:
		return 1 if packets[0] > packets[1] else 0
	elif t == 6:
		return 1 if packets[0] < packets[1] else 0
	elif t == 7:
		return 1 if packets[0] == packets[1] else 0
	else:
		return 0


# returns the index after packet has been processed
def parse_packet(binary: str) -> int:
	global index
	v = int(binary[index:index+meta_len], 2)
	t = int(binary[index+meta_len:index+2*meta_len], 2)
	index += meta_len * 2
	global version_sum
	version_sum += v
	value = 0
	if t == 4:
		value = parse_literal(binary)
	else:
		value = parse_operator(binary, t)
	return value

result = parse_packet(binary)

print('version_sum:', version_sum, 'result:', result)
