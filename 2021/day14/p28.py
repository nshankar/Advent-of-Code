from collections import defaultdict,Counter
with open("input.txt") as f:
	template = f.readline().rstrip()
	f.readline()
	rules = {}
	for line in f:
		pair, _, insert = line.split()
		rules[pair] = insert
n = 40
compressedTemplate = defaultdict(int)
for i in range(len(template)-1):
	couple = template[i:i+2]
	compressedTemplate[couple]+=1

for i in range(n):
	newCompressedTemplate = defaultdict(int)
	for couple in compressedTemplate:
		insert = rules[couple]
		a,b = couple
		newCompressedTemplate[a+insert] += compressedTemplate[couple]
		newCompressedTemplate[insert+b] += compressedTemplate[couple]
	compressedTemplate = newCompressedTemplate.copy()

c = defaultdict(int)
for key in compressedTemplate:
	a,b = key
	c[a] += compressedTemplate[key]
c[template[-1]]+= 1
print(max(c.values()) - min(c.values()))

