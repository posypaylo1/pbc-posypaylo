l = list(range(10))

def number_pairs(n):
    summ_ten = set([tuple(sorted([x, y])) for x in n for y in n if x + y == 10])
    return summ_ten
