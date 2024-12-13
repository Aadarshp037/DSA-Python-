                      # SELECTION SORT ALgorithm

def SelectionSort(A):
    s=len(A)
    for i in range(s-1):
        min_index=i
        for j in range(i+1,s):
            if A[j]<A[min_index]:
                min_index=j

        A[i],A[min_index]=A[min_index],A[i]
        print(A)

