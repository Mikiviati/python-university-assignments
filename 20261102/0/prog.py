def suum():
    s = i = 1
    while True:
        yield s
        i += 1
        s += 1 / (i*i)

def pargen():
    res = yield "START"
    while res:
        res = yield f"<{res}>"

    yield "STOP"

def walk2d():
    x, y = 0, 0
    while True:
        s = yield(x, y)
        dx, dy = s
        x += dx
        y += dy

def travel(n):
    for _ in range(n):
        yield "по кочкам"
    return "и в яму"

def travelwrap(n):
    x = yield from travel(n)
    yield x
    
from itertools import dropwhile, islice

def drop_slice():
    s = suum()

    f = dropwhile(lambda x: x <= 1.6, s)

    return list(islice(f, 10))


from itertools import filterfalse, count

def filterfls(n):
    f = filterfalse(lambda x: x % n == 0, count(1))
    return list(islice(f, 20))

from itertools import repeat, chain
def repeater(seq, n):
    for s in seq:
        yield from repeat(s, n)
from itertools import product
def prod():
    return [f"{x}{y}" for x, y in product('abcdefgh', range(1, 9))]







