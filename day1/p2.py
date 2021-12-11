with open("input.txt", encoding="utf-8") as f:
	data = [int(i) for i in f.readlines()]
step = 3
count = 0
for i in range(len(data)-step):
	if data[i+step] > data[i]:
		count += 1
print(count)