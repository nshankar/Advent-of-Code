def analyzeData(data):
	# ans[0] is the letters representing 1
	# ans[1] is the letters representing 4 \setminus alpha
	ans = []
	data = data.split()
	for d in data:
		if len(d) == 2:
			ans.append(set(d))
		elif len(d) == 4:
			ans.append(set(d))
	ans.sort(key=lambda x: len(x))
	ans[1] -= ans[0]
	return ans

def translateDigit(s,alpha,beta):
	s = set(s)
	if len(s) == 5:
		if alpha <= s:
			return "3"
		elif beta <= s:
			return "5"
		else:
			return "2"
	else: #if len(s) == 6
		if not alpha <= s:
			return "6"
		elif not beta <= s:
			return "0"
		else:
			return "9"

with open("input.txt") as f:
	lenToNum = {2:"1",3:"7",4:"4",7:"8"}
	score = 0
	for line in f:
		data, output = line.split('|')
		alpha,beta = analyzeData(data)
		digits = []
		for s in output.split():
			if len(s) in lenToNum:
				digits.append(lenToNum[len(s)])
			else:
				digit = translateDigit(s,alpha,beta)
				digits.append(digit)
		score += int("".join(digits))

	print(score)