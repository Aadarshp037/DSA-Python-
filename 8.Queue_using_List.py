             #QUEUE Using List

class Queue:
    def __init__(self):
        self.List=[]

    def is_empty(self):
        return len(self.List)==0
    
    def Enqueue(self,data):
        self.List.append(data)
    def Deqeue(self):
        if not self.is_empty():
            self.List.pop(0) 
        else:
            raise IndexError('Queue underflow')

    def get_front(self):
        if not self.is_empty():
            return self.List[0]
        else:
            raise IndexError('Queue underflow')
    def get_rear(self):
        if not self.is_empty():
            return self.List[-1]
        else:
            raise IndexError('Queue underflow')
    
    def size(self):
        return len(self.List)









