def MINF(*args):
    return lambda x: min(f(x) for f in args)


g = MINF(lambda x: x**2 + 1, lambda x: x**8)
print(g(int(input())))
