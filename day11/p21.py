from collections import deque
n = 10
threshhold = 9
nsteps = 10000

def updateData(data):
	q = deque()
	for i in range(n):
		for j in range(n):
			data[i][j] += 1
			if data[i][j] > threshhold:
				q.append((i,j))
	return q

def isValid(x,y):
	return x >= 0 and x < n and y >= 0 and y < n

def printData(data):
	for i in range(n):
		print(data[i])
	print()

def chainReaction(q, data, flashed):
	count = 0
	dirs = []
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			dirs.append((i,j))
	#breakpoint()
	while q:
		x,y = q.popleft()
		if flashed[x][y]:
			continue
		data[x][y] += 1
		if data[x][y] > 9:
			flashed[x][y] = True
			data[x][y] = 0
			for dx,dy in dirs:
				if isValid(x+dx,y+dy):
					q.append((x+dx,y+dy))
			count += 1
	return count

def main():
	with open("input.txt") as f:
		data = f.readlines()
	data = [[int(i) for i in list(row.rstrip())] for row in data]

	count = 0
	for _ in range(nsteps):
		flashed = [[False]*n for i in range(n)]
		q = updateData(data)
		#breakpoint()
		count = chainReaction(q,data,flashed)
		if count == n*n:
			return _ + 1
		#printData(data)
	return count

if __name__ == "__main__":
	print(main())

