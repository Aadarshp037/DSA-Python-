     #STACK using list
class Stack:
    def __init__(self,list=[]):
        self.list=list

    def is_empty(self):
        return len(self.list)==0
    
    def push_item(self,data):
        self.list.append(data)
    def pop(self):
        if not self.is_empty():
            self.list.pop()
        else:
            raise IndexError('Stack is empty')
    
    def peek(self):
        if not self.is_empty():
            print(self.list[-1])
        else:
            raise IndexError('Stack is empty')
    
    def size_of_stack(self):
        return print(len(self.list))
    

