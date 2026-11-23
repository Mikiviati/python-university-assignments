def multicall(num):
    def decor(fun):
        def newfun(*args):
            return [fun(*args) for _ in range(num)]
        return newfun
    return decor
