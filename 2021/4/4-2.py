import fileinput

filename = '4-input.txt'


nums = []
boards = []
board = []

i = -1
for line in fileinput.input(filename):
	if i == -1:
		nums = [int(x) for x in line.split(',')]
	elif i != 0:
		row = []
		for num in line.split():
			row.append([int(num), False])
		board.append(row)

		if i == 5:
			boards.append(board)
			board = []
			i = -1
	i += 1

winners = []
for i in range(len(boards)):
	winners.append(False)

winner = []
last = 0
for num in nums:
	for x in range(len(boards)):
		board = boards[x]
		if not winners[x]:
			for row in board:
				for pair in row:
						if pair[0] == num:
							pair[1] = True
			win = False
			for i in range(len(board)):
				if board[i][0][1] == True and board[i][1][1] == True and board[i][2][1] == True and board[i][3][1] == True and board[i][4][1] == True:
					win = True
					break
				if board[0][i][1] == True and board[1][i][1] == True and board[2][i][1] == True and board[3][i][1] == True and board[4][i][1] == True:
					win = True
					break
				
			if win:
				winners[x] = True
				winner = board
				last = num

total = 0
for row in winner:
	for pair in row:
		if pair[1] == False:
			total += pair[0]	
print(total*last)

