from math import *

def Calc(s, t, u):
    def f(x):
        a = eval(s)
        b = eval(t)
        return eval(u, globals(), {"x": a, "y": b})
    return f

s, t, u = eval(input())
x = eval(input())

print(Calc(s, t, u)(x))
