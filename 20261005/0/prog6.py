def f(a, b):
    return lambda x: a * x + b


g = f(*eval(input()))
print(g(10))
