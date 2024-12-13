             #Merge Sort

def Merge_Sort(A):
    if len(A)>1:
        s=len(A)//2
        Left=A[:s]
        right=A[s:]
        Merge_Sort(Left)
        Merge_Sort(right)

        print(Left)

        i=j=k=0 
        while i<len(Left) and j<len(right):
            if Left[i]<right[j]:
                A[k]=Left[i]
                i+=1
            else:
                A[k]=right[j]
                j+=1
            k+=1

        while i<len(Left):
            A[k]=Left[i]
            i+=1
            k+=1
     
    

X=[23,4,56,78,29,54,36,45,21,16,41]
Merge_Sort(X)
print(*X)

