from numpy import median,mean
from math import floor, ceil

def metric(nums, val):
	s = 0
	for n in nums:
		d = abs(val - n)
		s += d*(d+1)//2
	return s

with open("input.txt") as f:
	nums = [int(i) for i in f.readline().split(',')]	
	med = median(nums)
	ave = mean(nums)

	lo = min(floor(med), floor(ave))
	hi = max(ceil(med), ceil(ave))

	minFuel = float("inf")
	for val in range(lo,hi+1):
		minFuel = min(minFuel, metric(nums, val))
	print(minFuel)
	print(med, ave)