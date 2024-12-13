                 #Deque using Linked List Concept

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.items_count=0

    def is_empty(self):
        return self.items_count==0
    def insert_front(self,data):
        n=Node(data)
        n.next=self.front
        if not self.is_empty():
            self.front.prev=n
        else:
            self.rear=n
        self.front=n
        self.items_count+=1
    def insert_rear(self,data):
        n=Node(data)
        if not self.is_empty():
            n.next=None
            n.prev=self.rear
            self.rear.next=n
        else:
            self.front=n
        self.rear=n
        self.items_count+=1
    def delete_front(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
                self.items_count-=1
            else:
                self.front.next.prev=None
                self.front=self.front.next
                self.items_count-=1
        else:
            raise IndexError('Empty Deque')
        
    def delete_rear(self):
        if not self.is_empty():
            if self.items_count==1:
                self.front=None
                self.rear=None
                self.items_count-=1              
            else:
                self.rear=self.rear.prev
                self.rear.next=None
                self.items_count-=1
        else:
            raise IndexError('Empty Deque')
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            print(None)
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            return None
    
    def size(self):
        return self.items_count


X=Deque()
X.insert_front(20)

X.delete_front()

print('The size of Deque is',X.size())
print('The front element is',X.get_front())
print('The rear element is',X.get_rear())







