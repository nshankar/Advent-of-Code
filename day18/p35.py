from p35_helpers import *
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

def sanityCheck(root):
	first = getFirst(root)
	while first:
		print(first.val,end=' ')
		first = first.next
	print()

with open("input.txt") as f:
	snailFishSum = parseTree(f.readline())
	connectVals(snailFishSum)
	for line in f:
		num = parseTree(line)
		connectVals(num)
		snailFishSum = join(snailFishSum, num)
		reduce(snailFishSum)
	#breakpoint()
	#split(snailFishSum)
	printTree(snailFishSum)
	sanityCheck(snailFishSum)
	print(score(snailFishSum))

	#r = join(nums[0], nums[1])
	#reduce(r)
	#print(score(r))
	"""line = f.readline()
	snailFishSum = parseLinkedList(line)
	offset = 0
	for line in f:
		offset += join(snailFishSum, parseLinkedList(line))
		while True:
			printList(snailFishSum.head)
			if explode(snailFishSum, offset):
				continue
			elif split(snailFishSum):
				continue
			else:
				break"""
		


"""
def parseLinkedList(line):
	head = ListNode()
	curr = head
	depth = 0
	for c in line:
		if c == '[':
			depth += 1
		elif c == ']':
			depth -= 1
		elif c.isnumeric():
			curr.next = ListNode(val=[int(c), depth], prev=curr)
			curr = curr.next
	head.next.prev = None
	return LinkedList(head.next,curr)

def join(num1, num2):
	num1.tail.next = num2.head
	num1.tail = num2.tail
	return 1
def attachSentinal(num):
	s = ListNode([-1, -inf], None, num.head)
	num.head.prev = s 
	num.head = s

def explode(num,offset):
	attachSentinal(num)
	curr = num.head
	while curr:
		entry,depth = curr.val
		if depth+offset > 4:
			left = curr
			right = curr.next
			leftleft = curr.prev
			rightright = right.next if right else None
			res = ListNode([0,depth-1], leftleft, rightright)
			if leftleft:
				leftleft.val[0] += left.val[0]
				leftleft.next = res
			if rightright:
				rightright.val[0] += right.val[0]
				rightright.prev = res
			num.head = num.head.next
			return True
		curr = curr.next
	num.head = num.head.next
	return False

def split(num):
	attachSentinal(num)
	curr = num.head
	while curr:
		entry,depth = curr.val
		if entry > 9:
			left = ListNode([floor(entry/2), depth+1], curr.prev, None)
			right = ListNode([ceil(entry/2), depth+1], left, curr.next)
			left.next = right

			curr.prev.next = left
			if curr.next:
				curr.next.prev = right
			num.head=num.head.next
			return True
		curr = curr.next
	num.head=num.head.next
	return False
"""


"""





def explodeSolution(root):
	try:
		explodeTraversal(root, prev=None)
		return False #didn't explode
	except:
		return True #did explode

def explodeTraversal(nextNode, currNode, prevNode):
	if currNode.depth == 4:
		if prevNode
		left = .left.val
		right = node.right.val
		node.val = 0
		node.left=None
		node.right=None
		if prev:
			prev.val += left
		updateRight(node,right)
		raise Exception("kaboom")
	else:
		if node.val:
			prev = node
		explodeTraversal(node.left, prev,depth+1)
		explodeTraversal(node.right, prev, depth+1)

def updateRight(node,right):
	pass
"""




		
		
"""a = nums[0]
b = nums[1]
c = join(a,b)
printTree(c)
#breakpoint()
explodeSolution(c)
printTree(c)"""