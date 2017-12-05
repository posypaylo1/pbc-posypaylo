
def fib(n):
    lst=[0,1]
    if type(n) is not int:
        return []
    if n==0:
        return []
    elif n==1:
        return [0]
    a=0
    b=1
    for i in range(0,n-2):
        b=a+b
        a=b-a
        lst.append(b)
    return lst
