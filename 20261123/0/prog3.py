def istype(num):
    def decor(fun):
        def newfun(*args):
            if not all(isinstance(x, num) for x in args):
                raise TypeError
            return fun(*args)
        return newfun
    return decor
