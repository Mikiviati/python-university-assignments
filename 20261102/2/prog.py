from itertools import tee, islice

def slide(seq, n):
    if n <= 0:
        return

    a, b = tee(seq)
    while True:
        try:
            yield from islice(a, n)
            next(b)
            a, b = tee(b)
        except StopIteration:
            return

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
