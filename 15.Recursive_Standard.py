      # RECURSIVE Problems

def Naturalnumbers(n):
    if n>0:
        Naturalnumbers(n-1)
        print(n,end=' ')

def NaturalReverse(n):
    if n>0:
        print(n,end=' ')
        NaturalReverse(n-1)

def NaturalOdd(n):
    if n>0:
        NaturalOdd(n-1)
        print(2*n-1,end=' ')

def Naturaleven(n):
    if n>0:
        Naturaleven(n-1)
        print(2*n,end=(' '))


def NaturalOddReverse(n):
    if n>0:
        print(2*n-1,end=' ')
        NaturalOddReverse(n-1)
        
def NaturalevenReverse(n):
    if n>0:
        print(2*n,end=(' '))
        NaturalevenReverse(n-1)

def SumN(n):
    if n==1:
        return 1
    else:   
        s=n+(SumN(n-1))
        return s
       
def SumOdd(n):
    if n==1:
        return 1
    else:
        s=(2*n -1)+(SumOdd(n-1))
        return s

def SumEven(n):
    if n==1:
        return 2
    else:
        s=2*n +(SumEven(n-1))
        return s 
    
def Factorial(x):
    if x==1:
        return 1
    else:
        s=x*(Factorial(x-1))
        return s
    
def SumofSquare(n):
    if n==1:
        return 1
    else:
        s=(n*n)+(SumofSquare(n-1))
        return s

