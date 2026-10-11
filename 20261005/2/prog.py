def Minus(a, b):
    if isinstance(a, (list, tuple)) and type(a) is type(b):
        return type(a)(x for x in a if x not in b)
    return a - b

print(Minus(*tuple(eval(input()))))
