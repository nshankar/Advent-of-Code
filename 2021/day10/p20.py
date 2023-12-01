def checkIncomplete(line):
	mirror = {"[":"]", "(":")", "{":"}", "<":">"}
	stack = []
	for p in line:
		if p in mirror:
			stack.append(p)
		elif mirror[stack[-1]] == p:
			stack.pop()
		else:
			return []
	return stack

def computeScore(stack):
	score = 0
	points = {"(":1,"[":2,"{":3,"<":4}
	while stack:
		score *= 5
		score += points[stack.pop()]
	return score


with open("input.txt") as f:
	scores = []
	for line in f:
		stack = checkIncomplete(line.rstrip())
		score = computeScore(stack)
		if score:
			scores.append(score)
	scores.sort()
	mid = len(scores)//2
	print(scores[mid])