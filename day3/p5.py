def binIter2int(it):
	"""
	Convert boolean iterator to a base-10 integer 
	interpreting the boolean iterator as a binary number
	"""
	s = "".join(str(int(b)) for b in it)
	return int(s,2)

with open('input.txt',encoding='utf-8') as f:
	nums = [num.rstrip() for num in f.readlines()]
n, m = len(nums), len(nums[0])
counts = [0]*m
for i in range(n):
	for j in range(m):
		counts[j] += int(nums[i][j])
gamma = (counts[i] > n//2 for i in range(m))
epsilon = (counts[i] < n//2 for i in range(m))
print(binIter2int(gamma)*binIter2int(epsilon))