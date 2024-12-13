       #Assignment     Double Linked List

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=None
    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        a=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=a
        self.start=a
    
    def insert_at_last(self,data):
        if self.start is not None:
            temp=self.start
            m=Node(temp.next,data,None)
            while temp.next is not None:
                temp=temp.next
            temp.next=m
        else:
            m=Node(None,data,None)
            self.start=m

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
        

    def insert_after(self,temp,data):
        if temp is not None:
            a=Node(temp,data,temp.next)
            if temp.next is not None:
               temp.next=a
               a=temp.next.prev
            temp.next=a
        else:
            self.start=data

    
            


    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=(' '))
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
        
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None

        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None


    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

A=DLL()
A.insert_at_start(10)
A.insert_at_start(20)
A.insert_after(A.search(12),34)
for x in A:
    print(x)