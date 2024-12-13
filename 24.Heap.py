                   # HEAP

class Heap():
    def __init__(self):
        self.Heap=[]

    def CreateHeap(self,A):
        for x in A:
            self.insert(x)
        return self.Heap

    def insert(self,e):
        index=len(self.Heap)
        p=(index-1)//2
        while index>0 and self.Heap[p]<e:
            if index==len(self.Heap):
                self.Heap.append(self.Heap[p])
            else:
                self.Heap[index]=self.Heap[p]

            index=p
            p=(index-1)//2

        if index==len(self.Heap):
            self.Heap.append(e)
        else:
            self.Heap[index]=e

    def Top_element(self):
        if len(self.Heap)!=0:
            return self.Heap[0]
        
        else:
            raise EmptyHeapException()
        
    def Delete(self):
        if len(self.Heap)==0:
            raise EmptyHeapException()
        if len(self.Heap)==1:
            return self.Heap.pop(0)
        max_value=self.Heap[0]
        temp=self.Heap.pop()
        index=0
        Lindex=2*index +1
        Rindex=2*index +2

        while Lindex<len(self.Heap):
            if Rindex<len(self.Heap):
                if self.Heap[Lindex]>self.Heap[Rindex]:
                    if self.Heap[Lindex]>temp:
                        self.Heap[index]=self.Heap[Lindex]
                        index=Lindex
                    else:
                        break
                else:
                    if self.Heap[Rindex]>temp:
                        self.Heap[index]=self.Heap[Rindex]
                        index=Rindex
                    else:
                        break
                
            else: #No right child
                if self.Heap[Lindex]>temp:
                    self.Heap[index]=self.Heap[Lindex]
                    index=Lindex
                else:
                    break

            Lindex=2*index +1 
            Rindex=2*index +1

        self.Heap[index]=temp
        return max_value
    
    def HeapSort(self,A):
        self.CreateHeap(A)
        list2=[]
        try:
            while True:
                list2.insert(0,self.Delete())
        except EmptyHeapException:
            pass
        return(list2)
        
                  
                



        
class EmptyHeapException(Exception):
    def __init__(self,msg='Empty Heap'):
        self.msg=msg
    def __str__(self):
        return self.msg
    
C=Heap()
A=[23]
print(C.CreateHeap(A))
print(C.Delete())