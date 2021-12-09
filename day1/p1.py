count = 0
f = open("input.txt",'r')
prev = int(next(f))
for curr in f:
	curr = int(curr)
	if curr - prev > 0:
		count += 1
	prev = curr
f.close()
print(count)

