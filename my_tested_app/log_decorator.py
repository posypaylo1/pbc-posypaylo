def log(func):
    def wrapper(*args):
        for a in args:
            print('Input data: "{}"'.format(a))
        rs = func(*args)
        print("Works well")
        return rs
    return wrapper