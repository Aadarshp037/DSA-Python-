                      #Insertion Sort Algorithm

def InsertionSort(A):
    s=len(A)
    for i in range(1,s):
        temp=A[i]
        j=i-1
        while j>=0 and temp<A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp
        print(A)
