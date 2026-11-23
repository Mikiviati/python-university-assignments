from functools import wraps


def isint(fun):
    @wraps
    def f(*args):
        if not all(isinstance(x, int) for x in args):
            raise TypeError
        return fun(*args)
    return f
