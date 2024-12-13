       #   Stack inheriting List 

class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError('Stack is empty')
    def peek(self):
        if not self.is_empty():
            return print(self[-1])
        else:
            raise IndexError('Stack is empty')
        
    def size(self):
        return print(len(self))
    
    def insert(self,index,data):
        raise AttributeError('Insert has no attribute')
    

