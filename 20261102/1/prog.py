def fib(m, n):
    a, b = 1, 1

    for i in range(n + m):
        if i >= m:
            yield a

        a, b = b, a + b

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
