from collections import defaultdict
d = defaultdict(int)
count = 0
with open("input.txt") as f:
	for line in f:
		num = line[:-1]
		for i in range(len(num)):
			d[i] += int(num[i])
		count += 1

gammaRate = []
epsilonRate = []
for i in range(len(d)):
	gammaRate.append(int(d[i] > count//2))
	epsilonRate.append(int(d[i] < count//2))

gammaRate = "".join(str(x) for x in gammaRate)
epsilonRate = "".join(str(x) for x in epsilonRate)
gammaRate = int(gammaRate,2)
epsilonRate = int(epsilonRate, 2)
print(d)
print(gammaRate*epsilonRate)

