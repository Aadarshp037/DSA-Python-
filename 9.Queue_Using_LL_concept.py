        #QUEUE Using Linked Lst Concept
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.items_count=0

    def is_empty(self):
        return self.items_count==0
    
    def Enqueue(self,data):
        n=Node(data,self.front)
        if not self.is_empty():
            self.rear.next=n
        else:
            self.front=n
        self.rear=n
        self.items_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Empty Queue')
        elif self.front==self.rear:
            data=self.front.item
            self.front.item=None
            self.items_count-=1
            return data
        else:
            data=self.front.item
            self.front=self.front.next
            self.items_count-=1
            return data
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError('Empty Queue')
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError('Empty Queue')


    def size(self):
        return self.items_count
    

A=Queue()
A.Enqueue(20)
A.Enqueue(30)
A.Enqueue(45)
A.Enqueue(56)
print('The removed first element is ',A.dequeue())
print('The front element is ',A.get_front())
print('The rear element is ',A.get_rear())
print('The size of Queue is ',A.size())

    

