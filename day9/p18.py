def dfs(i,j,visited,count=0):
	#breakpoint()
	if (i < 0 or i >= len(visited) or j < 0 or j >= len(visited[0])) or visited[i][j]:
		return count
	visited[i][j] = True
	nbrs = [(0,1),(0,-1),(1,0),(-1,0)]
	tmp = 0
	for dx,dy in nbrs:
		tmp += dfs(i+dx,j+dy,visited,count)
	return 1 + tmp + count


with open("input.txt") as f:
	visited = []
	for line in f:
		#False iff in a basin
		visited.append([i == "9" for i in list(line.rstrip())])
	m = len(visited)
	n = len(visited[0])
	
	#breakpoint()
	s = 1
	basinSizes = []
	for i in range(m):
		for j in range(n):
			if not visited[i][j]:
				basinSizes.append(dfs(i,j,visited))
	basinSizes.sort(reverse=True)
	
	print(basinSizes[0]*basinSizes[1]*basinSizes[2])
