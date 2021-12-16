from collections import defaultdict
def isSmallCave(name):
	return name == name.lower()

def dfs(path,adjList,visited=defaultdict(set)):
	pos = path[-1]
	if pos == 'end':
		return 1
	if (pos in visited[1]|visited[2]) and visited[2]:
		return 0

	if isSmallCave(pos):
		if pos not in visited[1]:
			visited[1].add(pos)
		else:
			visited[1].remove(pos)
			visited[2].add(pos)

	count = 0
	for nbr in adjList[pos]:
		if nbr == 'start':
			continue
		path.append(nbr)
		count+= dfs(path,adjList,visited)
		path.pop()
	if isSmallCave(pos):
		if pos in visited[1]:
			visited[1].remove(pos)
		else:
			visited[2].remove(pos)
			visited[1].add(pos)
	return count


with open("input.txt") as f:
	edges = [edge.rstrip() for edge in f.readlines()]
	edges = [edge.split('-') for edge in edges]
	adjList = defaultdict(list)
	for a,b in edges:
		adjList[a].append(b)
		adjList[b].append(a)

	print(dfs(['start'], adjList))