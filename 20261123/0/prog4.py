from functools import wraps


class Istype():
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        @wraps(fun)
        def newfun(*args):
            if not all(isinstance(x, self.typ) for x in args):
                raise TypeError
            return fun(*args)
        return newfun
