                   #Binary Search while loop

def BinarySearch(list,low,high,data):

    while low<=high:
        mid= low + (high-low)//2
        if list[mid]==data:
            return mid
        elif list[mid]<data:
            high= mid-1
        elif list[mid]>data:
            low=mid+1
    else:
        return -1
    
A=[24,34,56,8,23,78,98]
A.sort()
x=int(input('Enter the number to search for: '))
a=BinarySearch(A,0,len(A)-1,x)
if a==-1:
    print('Element is not found')
else:
    print('The element is present at index: ',a)