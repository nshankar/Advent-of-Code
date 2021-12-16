
def buildFoldFunction(idx, val):
	fold,mult = [0,0],[1,1]
	fold[idx] = val
	mult[idx] = -1
	def foldFunction(coord):
		if coord[idx] > fold[idx]:
			return tuple(2*fold[i] + mult[i]*coord[i] for i in range(2))
		return coord
	return foldFunction

with open("input.txt") as f:
	coords, folds = set(), []
	coordLines = True
	for line in f.readlines():
		if line == "\n":
			coordLines = False
			continue
		if coordLines:
			a,b = line.rstrip().split(',')
			coords.add((int(a),int(b)))
		else:
			z,val= line.split()[-1].split('=')
			idx = 0 if z=='x' else 1
			folds.append(buildFoldFunction(idx, int(val)))
	
	for fold in folds:
		newCoords = set()
		for coord in coords:
			newCoords.add(fold(coord))
		coords = newCoords.copy()
	
	## draw letters
	import matplotlib.pyplot as plt
	x = [x for x,y in coords]
	y = [-y for x,y in coords]
	plt.figure(figsize=(10,1))
	plt.scatter(x,y,c='r')
	plt.show()
