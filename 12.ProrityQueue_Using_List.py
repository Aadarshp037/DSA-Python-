              #Priority Queue Using List
class PriorityQueue:
    def __init__(self):
        self.A=[]

    def is_empty(self):
        return len(self.A)==0
    def push(self,data,priority):
        index=0
        while index<len(self.A) and self.A[index][1]<=priority:
            index+=1
        self.A.insert(index,(data,priority))
    
    def pop(self):
        if self.is_empty():
            raise IndexError('PriorityQueue is empty')
        data=self.A[0][0]
        self.A.pop(0)
        return data
    def size(self):
        return len(self.A)

A=PriorityQueue()
A.push(20,1)
A.push(34,5)
A.push(23,2)
for i in range(A.size()):
    print(A.pop())

print(A.size())


