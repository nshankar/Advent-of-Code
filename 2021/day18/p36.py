from p35_helpers import *
import copy
from math import floor, ceil


#Broad idea: Build tree with stack, make a generator that yields the next value to the right using dfs with a stack
# split is easy, compute score is easy

def parseTree(line):
	root = Node()
	stack = [root]
	for c in line:
		node = stack[-1]
		if c == '[':
			node.left = Node()
			stack.append(node.left)
		elif c.isnumeric():
			node.val = int(c)
		elif c == ',':
			stack.pop()
			node = stack[-1]
			node.right = Node()
			stack.append(node.right)
		elif c == ']':
			stack.pop()
	return root

def connectVals(root):
	stack = [root]
	prev = None
	while stack:
		node = stack.pop()
		if node.val is not None:
			node.prev = prev
			if prev: prev.next = node 
			prev = node
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return

def getFirst(root):
	stack = [root]
	while stack:
		node = stack.pop()
		if node.val is not None:
			return node
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return None

def getLast(root):
	stack = [root]
	while stack:
		node = stack.pop()
		if node.val is not None:
			return node
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)
	return None

def join(root1,root2):
	first2 = getFirst(root2)
	last1 = getLast(root1)
	#if not first2.val:
	#	print("Error Joining, root2 has no first val")
	last1.next = first2
	first2.prev = last1
	newRoot = Node(val=None,left=root1, right=root2)
	return newRoot

def explode(root):
	try:
		explodeHelper(root)
		return False #didn't explode
	except:
		return True #did explode

def explodeHelper(root, depth=0):
	if root is None:
		return
	if depth == 4 and root.left:
		left = root.left
		right = root.right
		leftleft = left.prev
		rightright = right.next if right else None
		if leftleft:
			leftleft.val += left.val
			leftleft.next = root
		if rightright:
			rightright.val += right.val
			rightright.prev = root
		root.prev = leftleft
		root.next = rightright
		root.val = 0
		root.left = root.right = None
		raise Exception("kaboom")

	explodeHelper(root.left, depth+1)
	explodeHelper(root.right, depth+1)

def split(root):
	first = getFirst(root)
	while first:
		if first.val >= 10:
			prev = first.prev
			next = first.next
			val = first.val
			first.val = None
			first.left = Node(val=floor(val/2), prev=prev,next=None)
			first.right = Node(val=ceil(val/2), prev=first.left,next=next)
			first.left.next = first.right
			if prev:
				prev.next = first.left
			if next:
				next.prev = first.right
			return True
		first=first.next
	return False

def reduce(root):
	while True:
		#printTree(root)
		#sanityCheck(root)
		if explode(root):
			continue
		elif split(root):
			continue
		else:
			break

def score(root):
	if root is None:
		return 0
	if root.val is not None:
		return root.val
	return 3*score(root.left) + 2*score(root.right)

def scoreOfSum(root1, root2):
	total = join(root1,root2)
	reduce(total)
	return score(total)

def sanityCheck(root):
	first = getFirst(root)
	while first:
		print(first.val,end=' ')
		first = first.next
	print()




with open("input.txt") as f:
	nums = []
	for line in f:
		num = parseTree(line)
		connectVals(num)
		nums.append(num)
	maxScore = 0
	for num1 in nums:
		for num2 in nums:
			maxScore = max(maxScore, scoreOfSum(copy.deepcopy(num1), copy.deepcopy(num2)))
	print(maxScore)


