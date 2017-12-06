import argparse


def log(func):
    def wrapper(*args):
        for a in args:
            print('Tested input: "{}"'.format(a))
        rs = func(*args)
        print("Works well")
        return rs
    return wrapper

@log
def fib(n):
    lst=[0,1]
    if type(n) is not int:
        return []
    if n<=0:
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Returns given item amount of Fibonacci sequence")
    parser.add_argument("-n", "--number", type=int, help="The required amount of sequence items")
    args = parser.parse_args()
    print(fib(args.number))



