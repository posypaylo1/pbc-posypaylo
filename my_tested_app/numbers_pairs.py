import argparse

def log(func):
    def wrapper(*args):
        for a in args:
            print('Number of items in the list: "{}"'.format(a))
        rs = func(*args)
        print("Works well")
        return rs
    return wrapper

@log
def number_pairs(n):
    lst = list(range(n))
    summ_ten = set([tuple(sorted([x, y])) for x in lst for y in lst if x + y == 10])
    return summ_ten


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="returns unique pairs of numbers which sum is = 10 for"
                                                 " a given collection of numbers")
    parser.add_argument("-l", "--list", type=int, help="Enter number of items to generate list")
    args = parser.parse_args()
    print(number_pairs(args.list))


