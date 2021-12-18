#WOLOG xtarget is a positive range
xtarget = [111,161]
ytarget = [-154,-101]


def gaussSum(n):
	return n*(n+1)//2

print(gaussSum(15)) #check x range is possible
print(gaussSum(abs(min(ytarget))-1)) #get optimal y height (requires x range to be 'nice' and ytarget to be negative)