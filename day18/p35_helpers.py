class Node:
	def __init__(self, val=None, left=None,right=None, prev=None, next=None):
		self.val = val
		self.left = left
		self.right = right
		self.prev = prev
		self.next = next

	"""
	def copy(self, node = Node()):
		if node is None:
			return None
		left = self.copy(self.left)
		right = self.copy(self.right)
		node.val = self.val
		node.left = left 
		node.right = right 
		return node
	"""

class ListNode:
	def __init__(self, val=0, prev=None, next=None):
		self.val = val
		self.prev = prev
		self.next = next

class LinkedList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

def printTree(node):
	printTreeHelper(node)
	print()

def printTreeHelper(node,depth=0):
	if node is None:
		return
	print(node.val, end=' ')
	#print((node.val,depth),end=' ')
	printTreeHelper(node.left,depth+1)
	printTreeHelper(node.right,depth+1)

def printList(node):
	while node is not None:
		print(node.val, end=' ')
		node = node.next
	print()