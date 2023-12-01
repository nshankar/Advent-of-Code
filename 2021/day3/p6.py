def myBisect(l, lo=0, hi=None):
	"""
	Return index of first 1 in l[lo:hi]
	Requires: l sorted and contains only 0s and 1s
	"""
	if hi is None: hi = len(l)
	while(lo < hi):
		mid = lo + (hi-lo)//2
		if l[mid]: hi = mid 
		else: lo = mid + 1
	return lo

def helper(nums, findMostCommon):
	"""
	Main logic, see spec
	"""
	digit = 0
	bot,top = 0,len(nums[0])
	while (bot+1 < top):
		col = nums[digit]
		idx = myBisect(col, bot, top)
		bot, top = updateRange(idx,bot,top,findMostCommon)
		digit+=1
	return bot

def updateRange(idx, bot, top, findMostCommon):
	"""Updates range to only include most/least common"""
	if findMostCommon == (idx-bot > (top-bot)//2):
		top = idx
	else:
		bot = idx
	return bot,top

def reformat(nums):
	"""Transpose and change types"""
	newNums = []
	for j in range(len(nums[0])):
		col = [int(nums[i][j]) for i in range(len(nums))]
		newNums.append(col)
	return newNums

with open("test.txt",encoding="utf-8") as f:
	_nums = [_num.rstrip() for _num in f.readlines()]
_nums.sort()
nums = reformat(_nums) #worthwhile so that helper() runs in linearithmic time
g_idx = helper(nums,findMostCommon=True)
s_idx = helper(nums,findMostCommon=False)
print(int(_nums[g_idx],2)*int(_nums[s_idx],2))