#also solves p10 by adjusting fill
import re 

def fill(arr,x1,y1,x2,y2):
	if x1 == x2:
		y1,y2 = sorted([y1,y2])
		for y in range(y1, y2+1):
			arr[x1][y] += 1
	elif y1 == y2:
		x1,x2 = sorted([x1,x2])
		for x in range(x1,x2+1):
			arr[x][y1] += 1
	else:
		dx = (x2 - x1)//abs(x2-x1)
		dy = (y2 - y1)//abs(y2-y1)
		while x1 != x2:
			arr[x1][y1] += 1
			x1 += dx
			y1 += dy
		arr[x2][y2] += 1




n = 1000
arr = [[0]*n for i in range(n)]

with open("input.txt") as f:
	for line in f:
		coords = [int(n) for n in re.findall(r'\d+', line)]
		fill(arr, *coords)
	#for i in range(n):
	#	print(arr[i])
	count = 0
	for i in range(n):
		for j in range(n):
			if arr[i][j] > 1:
				count += 1
	print(count)
