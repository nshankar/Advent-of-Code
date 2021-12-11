def lowPoint(data,x,y):
	nbrs = [(0,1),(0,-1),(1,0),(-1,0)]
	for dx,dy in nbrs:
		if data[x][y] >= data[x+dx][y+dy]:
			return 0
	return data[x][y] + 1

with open("input.txt") as f:
	data = []
	n = -1
	for line in f:
		line = [int(i) for i in list(line.rstrip())]
		if data == []:
			n = len(line)
			data.append([float("inf")]*(n+2))
		data.append([float("inf")] + line+ [float("inf")])
	data.append([float("inf")]*(n+2))

	for i in range(len(data)):
		print(data[i])
	#print(len(data), len(data[0]))
	s = 0
	for i in range(1, len(data)-1):
		for j in range(1, len(data[0])-1):
			s+= lowPoint(data,i,j)
	print(s)
