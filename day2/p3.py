from collections import defaultdict
d = defaultdict(int)
with open("input.txt") as f:
	for line in f:
		d[line[0]] += int(line[-2])
print(d)
print(d['f'] * (d['d'] - d['u']))

