def log(func):
    def wrapper(*args):
        print("{}{}".format(func.__name__, args))
        return func(*args)
    return wrapper