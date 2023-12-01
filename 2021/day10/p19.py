def checkCorrupted(line):
	mirror = {"[":"]", "(":")", "{":"}", "<":">"}
	stack = []
	for p in line:
		if p in mirror:
			stack.append(p)
		elif mirror[stack[-1]] == p:
			stack.pop()
		else:
			return p
	return ""

with open("input.txt") as f:
	points = {"":0, ")":3, "]":57, "}":1197, ">":25137}
	score = 0
	for line in f:
		p = checkCorrupted(line.rstrip())
		score += points[p]
	print(score)
