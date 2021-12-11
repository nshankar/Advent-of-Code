with open("input.txt",encoding="utf-8") as f:
	fwd,aim,depth = 0,0,0
	for line in f:
		key, n = line[0], int(line[-2])
		if key == 'd':
			aim += n
		elif key == 'u':
			aim -= n 
		else:
			fwd += n 
			depth += n*aim
print(fwd*depth)