from log_decorator import log


@log
def number_pairs(*args):
    lst = [number for number in args if type(number) is int or type(number) is float]
    summ_ten = set([tuple(sorted([x, y])) for x in lst for y in lst if x + y == 10])
    return summ_ten





