dirs = {'f':0,'d':0,'u':0}
with open("input.txt",encoding="utf-8") as f:
	for line in f:
		dirs[line[0]] += int(line[-2])
print(dirs['f'] * (dirs['d'] - dirs['u']))

