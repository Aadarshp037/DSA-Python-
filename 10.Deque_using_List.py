            #DEQUE Using List

class Deque:
    def __init__(self):
        self.List=[]

    def is_empty(self):
        return len(self.List)==0
    def insert_front(self,data):
        self.List.insert(0,data)
    def insert_rear(self,data):
        self.List.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.List.pop(0)
        else:
            raise  IndexError('list is Empty')

    def delete_rear(self):
        if not self.is_empty():
            self.List.pop()
        else:
            raise  IndexError('list is Empty')
        
    def get_front(self):
        if not self.is_empty():
            return self.List[0]
        else:
            raise  IndexError('list is Empty')
            
    def get_rear(self):
        if not self.is_empty():
            return self.List[-1]
        else:
            raise  IndexError('list is Empty')
        
    def size(self):
        return len(self.List)

A=Deque()
A.insert_front(20)
A.insert_front(30)
A.insert_rear(34)
A.insert_rear(18)
A.delete_rear()
A.delete_front
print('The front element is ',A.get_front())
print('The rear element is ',A.get_rear())
print(A.size())

    
