
def fib(n):
    lst=[0,1]
    if n==0:
        return lst[0]
    elif n==1:
        return lst
    a=0
    b=1
    for i in range(0,n-1):
        b=a+b
        a=b-a
        lst.append(b)
    print(lst)

fib(5)