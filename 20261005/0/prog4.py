def binN(n, ones, base=1):
    if n == 0:
        if ones == 0:
            print(base)
        return
    if ones:
        binN(n - 1, ones - 1, base * 2 + 1)
    binN(n - 1, ones, base * 2)


print(binN(*eval(input())))
