import argparse
from my_tested_app import number_pairs
from my_tested_app import fib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="App returns a fibonacci sequence of set length or "
                                                 "creates pairs of inputed numbers which sum is 10")
    group = parser.add_argument_group("Parameters")
    parser.add_argument('-a', '--app', type=str, required=True, help='Apps to run: fib or number')
    group.add_argument("-n", "--number", type=int, help="Enter number to get equal fibonacci items ", required=False,
                        action='store')
    group.add_argument("-l", "--length", type=int, help="Enter sequence of numbers, use 'space' as divider",
                       nargs='+', required=False, action='store')
    args = parser.parse_args()
    if args.app == "fib":
        print(fib(args.number))
    elif args.app == "number":
        print(number_pairs(*args.length))
