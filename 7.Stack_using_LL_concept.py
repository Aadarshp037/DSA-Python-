      #STACK using Linked List Concept


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.count=0

    def is_empty(self):
        return self.start==None

    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.count+=1

    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.count-=1
            return data
        else:
            raise IndexError
    def peek(self):
        if not self.is_empty():
            print(self.start.item)
        else:
            raise IndexError('List is Empty')
        
    def size(self):
        return self.count
    
