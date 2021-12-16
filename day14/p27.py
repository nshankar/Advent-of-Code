from collections import Counter
with open("input.txt") as f:
	template = f.readline().rstrip()
	f.readline()
	rules = {}
	for line in f:
		pair, _, insert = line.split()
		rules[pair] = insert
n = 10
for i in range(n):
	newTemplate = []
	for j in range(len(template)-1):
		curr = template[j]
		nex = template[j+1]
		newTemplate.append(curr+rules[curr+nex])
	newTemplate.append(nex)
	template = "".join(newTemplate)
c = Counter(template)
print(max(c.values()) - min(c.values()))

