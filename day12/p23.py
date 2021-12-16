def dfs(path, adjList, visited=set()):
	pos = path[-1]
	if pos == 'end':
		return 1
	if pos in visited:
		return 0

	if pos == pos.lower():
		visited.add(pos)
	count = 0
	for nbr in adjList[pos]:
		count+= dfs(path+[nbr], adjList, visited)
	if pos == pos.lower():
		visited.remove(pos)
	return count

from collections import defaultdict
with open("input.txt") as f:
	edges = [edge.rstrip() for edge in f.readlines()]
	edges = [edge.split('-') for edge in edges]
	adjList = defaultdict(list)
	for a,b in edges:
		adjList[a].append(b)
		adjList[b].append(a)
	print(dfs(['start'], adjList))