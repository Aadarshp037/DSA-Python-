              # QUICK SORT

def QuickSort(A):
    if len(A)<=1:
        return A
    else:
        pivot=A[0]
        lesser=[x for x in A[1:] if x<pivot]
        greater=[x for x in A[1:] if x>=pivot]
        return QuickSort(lesser) + [pivot] + QuickSort(greater)

