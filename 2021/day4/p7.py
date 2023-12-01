#also solves p8 with very minor changes

n = 5
def movesToWin(board,numbers):
	rows = [0]*5
	cols = [0]*5
	diags = [0]*2
	for m in range(len(numbers)):
		n = numbers[m]
		if n in board:
			i, j = board[n]
			rows[i] += 1
			cols[j] += 1
			if i == j:
				diags[0] += 1
			if i == n - j - 1:
				diags[1] += 1
			if rows[i] == 5 or cols[j] == 5 or 5 in diags:
				return m + 1
	return 25

def computeScore(board,numbers):
	for n in numbers:
		if n in board:
			del board[n]
	s = 0
	for key in board:
		s += key
	return s*numbers[-1]

def getBoard(stream):
	b = {}
	n=5
	for i in range(n):
		row = stream.readline().split()
		for j in range(n):
			b[int(row[j])] = (i,j)
	return b


with open("input.txt") as f:
	numbers = f.readline()
	numbers = [int(s) for s in numbers.split(',')]
	#minBoard = {}
	#minMoves = 25
	maxBoard = {}
	maxMoves = 0
	while f.read(1):
		board = getBoard(f)
		moves = movesToWin(board, numbers)
		if moves > maxMoves:
			maxMoves = moves
			maxBoard = board.copy()


	print(computeScore(maxBoard,numbers[:maxMoves]))