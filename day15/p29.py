from math import inf
def getNbrs(loc):
	x,y = loc
	dirs = [(0,1), (1,0), (0,-1), (-1,0)]
	ans = []
	for dx,dy in dirs:
		if 0<=x+dx<m and 0<=y+dy<n:
			ans.append((x+dx,y+dy))
	return ans

with open("input.txt") as f:
	risk = [list(map(int,line.rstrip())) for line in f.readlines()]

## Solve with Dijkstra
m,n = len(risk), len(risk[0])
start = (0,0)
target = (m-1,n-1)
dists = [[inf]*n for i in range(m)]
dists[0][0] = 0
known = set([start])
seen = set()
for nbr in getNbrs(start):
	seen.add(nbr)
	i,j = nbr
	dists[i][j] = risk[i][j]

while start != target:
	_,x,y = min(((dists[i][j],i,j) for i,j in seen), key=lambda x: x[0])
	seen.remove((x,y))
	known.add((x,y))
	for nbr in getNbrs((x,y)):
		if nbr not in known:
			seen.add(nbr)
		i,j = nbr
		dists[i][j] = min(dists[i][j], dists[x][y] + risk[i][j])
	start = (x,y)

for i in range(m):
	print(dists[i])
print(dists[m-1][n-1])





