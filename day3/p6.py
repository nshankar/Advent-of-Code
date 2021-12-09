from collections import defaultdict
from bisect import bisect_left, bisect_right

with open("input.txt") as f:
	lines = [line[:-1] for line in f.readlines()]
	lines.sort()
	lo = 0
	hi = len(lines)
	for i in range(len(lines[0])):
		if lo+1 == hi:
			break
		tmp = [int(line[i]) for line in lines]
		mid = lo + (hi-lo)//2
		mostCommon = tmp[mid]		
		if mostCommon:
			idx = bisect_left(tmp,mostCommon,lo=lo, hi=hi)
			lo = idx
		else:
			idx = bisect_right(tmp,mostCommon, lo=lo, hi=hi)
			hi = idx
	if lo+1 == hi:
		g = lines[lo]
		print("Generator Rating", lines[lo])

	lo = 0
	hi = len(lines)
	for i in range(len(lines[0])):
		if lo+1 == hi:
			break
		tmp = [int(line[i]) for line in lines]
		nZeros = bisect_right(tmp, 0, lo, hi) - lo
		#print(nZeros)
		if nZeros <= (hi-lo)//2:
			leastCommon = 0
		else:
			leastCommon = 1
		#mid = lo + (hi-lo)//2
		#leastCommon = int(not tmp[mid])	
		if leastCommon:
			idx = bisect_left(tmp,leastCommon,lo=lo, hi=hi)
			lo = idx
		else:
			idx = bisect_right(tmp,leastCommon, lo=lo, hi=hi)
			hi = idx
	if lo+1 == hi:
		s = lines[lo]
		print("Scrubber Rating", lines[lo])

	print(int(g,2)*int(s,2))




	"""
	Slines = Glines.copy()
	GRating = 0
	SRating = 0
	counts = defaultdict(int)
	count = len(Glines)
	for line in Glines:
		for i in range(len(line)):
			counts[i] += int(line[i])

	for i in range(len(counts)):
		print(i)
		print(Glines)
		print(Slines)
		if len(Glines) == 1:
			GRating = Glines.pop()
		if len(Slines) == 1:
			SRating == Slines.pop()
		Gdigit = int(counts[i] >= count//2)
		Sdigit = int(not Gdigit)
		Glines = {x for x in Glines if int(x[i]) == Gdigit}
		Slines = {x for x in Slines if int(x[i]) == Sdigit}

	print(GRating,SRating)"""