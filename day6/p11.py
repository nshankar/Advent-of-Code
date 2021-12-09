newFishCycle = 8
days = 256
count = [0]*(newFishCycle+1)

with open("input.txt") as f:
	fish = [int(i) for i in f.readline().split(',')]
for n in fish:
	count[n] += 1

for d in range(days):
	newFish = count[0] 
	count[:7] = count[1:7] + [count[0]]
	count[6] += count[7]
	count[7] = count[8]
	count[8] = newFish
print(sum(count))

