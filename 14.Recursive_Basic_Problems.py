                      # RECURSION Problems

#1 Print first natural numbers upto n

def f1(n):
    if n==1:
        A.append(1)
    else:
        A.append(n)
        f1(n-1)

A=[]
f1(int(input("Enter the value of n :")))
A.sort()
print('The naturals number upto',len(A))
for x in A:
    print(x,end=" ")

#2 Print first natural numbers upto n in reverse order

def f1(n):
    if n==1:
        A.append(1)
    else:
        A.append(n)
        f1(n-1)

A=[]
f1(int(input("Enter the value of n :")))
print('The naturals number upto',len(A))
for x in A:
    print(x,end=" ")

#3 Print first odd natural numbers upto n

def f1(n):
    if n==1:
        A.append(1)
    else:
        s=2*n -1
        A.append(s)
        f1(n-1)
A=[]
f1(int(input('first  odd naturals number ')))
A.sort()
for x in A:
    print(x,end=" ")

#4 Print first n even natural numbers 

def f1(n):
    if n==1:
        return A.append(2)
    else:
       s=2*n
       A.append(s)
       f1(n-1)
A=[]
f1(int(input('First n natural even numbers :')))
A.sort()
for x in A:
    print(x,end=" ")

#5 Print first odd natural numbers upto n in reverse order

def f1(n):
    if n==1:
        A.append(1)
    else:
        s=2*n -1
        A.append(s)
        f1(n-1)
A=[]
f1(int(input('first  odd naturals number ')))
for x in A:
    print(x,end=" ")

#4 Print first n even natural numbers in reverse order

def f1(n):
    if n==1:
        return A.append(2)
    else:
       s=2*n
       A.append(s)
       f1(n-1)
A=[]
f1(int(input('First n natural even numbers :')))
for x in A:
    print(x,end=" ")
   



