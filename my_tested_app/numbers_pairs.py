import argparse
from log_decorator import log


@log
def number_pairs(*args):
    lst = [number for number in args if type(number) is int or type(number) is float]
    summ_ten = set([tuple(sorted([x, y])) for x in lst for y in lst if x + y == 10])
    return summ_ten


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="returns unique pairs of numbers which sum is = 10 for"
                                                 " a given sequence of numbers")
    group = parser.add_argument_group("Parameters")
    group.add_argument("-l", "--list", type=set, help="Enter number of items to generate list", nargs='+', required=True)
    args = parser.parse_args()
    print(number_pairs(*args.list))


