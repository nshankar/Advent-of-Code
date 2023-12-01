from math import inf
import heapq

def getNbrs(loc):
	x,y = loc
	dirs = [(0,1), (1,0), (0,-1), (-1,0)]
	ans = []
	for dx,dy in dirs:
		if 0<=x+dx<m and 0<=y+dy<n:
			ans.append((x+dx,y+dy))
	return ans

def increaseMap(risk, mult=5):
	m,n = len(risk), len(risk[0])
	newRisk = [[None]*(5*n) for i in range(5*m)]
	for i in range(5*m):
		for j in range(5*n):
			offset = i//m + j//n 
			newRisk[i][j] = risk[i%m][j%n] + offset
			while newRisk[i][j] > 9:
				newRisk[i][j] -= 9
	return newRisk

with open("input.txt") as f:
	risk = [list(map(int,line.rstrip())) for line in f.readlines()]
risk = increaseMap(risk)

## Solve with Dijkstra
m,n = len(risk), len(risk[0])
curr = (0,0)
target = (m-1,n-1)
dists = [[inf]*n for i in range(m)]
dists[0][0] = 0
known = set([curr])
seen = []
for i,j in getNbrs(curr):
	dists[i][j] = risk[i][j]
	heapq.heappush(seen, (dists[i][j],i,j))

while curr != target:
	_,x,y = heapq.heappop(seen)
	if (x,y) in known:
		continue
	for i,j in getNbrs((x,y)):
		dists[i][j] = min(dists[i][j], dists[x][y] + risk[i][j])
		heapq.heappush(seen, (dists[i][j],i,j))

	curr = (x,y)
	known.add((x,y))
#for i in range(m):#
#	print(dists[i])
print(dists[m-1][n-1])