          #     Circular Double Linked List

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    def insert_start(self,data):
        n=Node(data)
        if not self.is_empty():
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        else:
            n.next=n
            n.prev=n
            
        self.start=n

    def insert_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.prev=self.start.prev
            n.next=self.start
            n.prev.next=n
            self.start.prev=n

    def search(self,data):
        temp=self.start
        if temp is None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None    
    
    def insert_after(self,temp,data):
        n=Node(data)
        if temp is not None:
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n
        
    def print_items(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=(' '))
            temp=temp.next
            while temp!=self.start:
                print(temp.item,end=(' '))
                temp=temp.next
        
    def delete_first(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next

    def delete_last(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def delete_item(self,data):
        if not self.is_empty():
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp!=self.start:
                    if temp.item==data:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                    temp=temp.next

    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data


A=CDLL()
A.insert_start(10)
A.insert_last(40)
A.insert_last(45)
A.insert_after(A.search(10),34)
A.delete_last()
A.print_items()




