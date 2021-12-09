fwd = 0
aim = 0
depth = 0
with open("input.txt") as f:
	for line in f:
		a = line[0]
		n = int(line[-2])
		if a == 'd':
			aim += n
		elif a == 'u':
			aim -= n 
		else:
			fwd += n 
			depth += n*aim
print(fwd, aim, depth)
print(fwd*depth)