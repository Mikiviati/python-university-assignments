def dumper(f):
    def newfun(*args):
        print(">", args)
        res = f(*args)
        print("<", res)
        return res
    return newfun
