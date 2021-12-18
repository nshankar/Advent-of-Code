from math import ceil,sqrt
#WOLOG xtarget is a positive range
#WOLOG ytarget is a negative range
xtarget = [111,161]
ytarget = [-154,-101]

def gaussSum(n):
	return n*(n+1)//2

def getFeasibleVels():
	#n^2 + n - 2*c > 0
	# has n = (-1 +- sqrt(1 + 9c))/2
	xVelMin = ceil((-1 + sqrt(1+9*xtarget[0])/2))
	return range(xVelMin, xtarget[1]+1), range(min(ytarget), -min(ytarget))


def update(x,y,vx,vy):
	x+= vx
	y+= vy
	vx+= -vx//abs(vx) if vx else 0
	vy+= -1
	return x,y,vx,vy

def isFeasible(x,y):
	if x <= xtarget[1] and y >= ytarget[0]:
		return True
	return False

def isSolution(x,y):
	if xtarget[0] <=x<= xtarget[1] and ytarget[0]<=y<=ytarget[1]:
		return True
	return False

def main():
	solutions = 0
	xVels, yVels = getFeasibleVels()
	#print(xVels, yVels)
	for Vx in xVels:
		for Vy in yVels:
			x,y,vx,vy = 0,0,Vx,Vy
			while(isFeasible(x,y)):
				if isSolution(x,y):
					solutions += 1
					break
				x,y,vx,vy=update(x,y,vx,vy)
	print(solutions)

if __name__=="__main__":
	main()

