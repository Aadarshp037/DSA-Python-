                 #Bubble sort Algorithm


def BubbleSort(A):
    s=len(A)
    for i in range(s-1):
        for j in range(1,s-i):
            if A[j-1]<=A[j]:
                pass
            else:
                A[j-1],A[j]=A[j],A[j-1]

        print(A)
    print('The sorted elements are',A)


def ModifiedBubbleSort(A):
    s=len(A)
    for i in range(s-1):
        count=0
        for j in range(1,s-i):
            if A[j-1]<=A[j]:
                pass
            else:
                A[j-1],A[j]=A[j],A[j-1]
                count=1           
        if count==0:
            break
        print(A)
        
    print('The sorted element',A)

