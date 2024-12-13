        #Prority Queue Using Linked List Concept

class Node:
	def __init__(self,item=None,next=None,priority=None):
		self.item=item
		self.next=next
		self.priority=priority

class PQueue:
	def __init__(self):
		self.start=None
		self.items_count=0
	def is_empty(self):
		return self.start==None
	def push(self,data,P):
		n=Node(data,None,P)
		if self.is_empty() or self.start.priority>P:
			n.next=self.start
			self.start=n
			self.items_count+=1
		else:
			temp=self.start
			while temp is not None:
				if temp.priority<=P and temp.next==None:
					temp.next=n
					break
				if temp.priority<=P and temp.next.priority>P:
					n.next=temp.next
					temp.next=n
					break
				temp=temp.next
			self.items_count+=1
	def pop(self):
		if self.is_empty():
			raise IndexError('Queue has No elements')
		data=self.start.item
		self.start=self.start.next
		self.items_count-=1
		return data
				
				
	def size(self):
			return self.items_count
			
A=PQueue()
A.push(20,4)
A.push(34,3)
A.push(45,3)

for i in range(A.size()):
	print(' The popped element is',A.pop())