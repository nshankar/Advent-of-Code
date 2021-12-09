count = 0
f = open("input.txt",'r')
a = int(next(f))
b = int(next(f))
c = int(next(f))
for d in f:
	d = int(d)
	#print(a,b,c,d)
	if d - a > 0:
		#print("increase")
		count += 1
	a = b
	b = c
	c = d
f.close()
print(count)