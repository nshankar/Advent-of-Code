from numpy import median
with open("input.txt") as f:
	nums = [int(i) for i in f.readline().split(',')]	
	med = median(nums)
	ans = 0
	for n in nums:
		ans += abs(n - med)
	print(ans)