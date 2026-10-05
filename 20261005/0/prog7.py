def gen(n):
    adders = []
    for i in range(n):
        def adder(x):
            return x + i
        adders.append(adder)
    return adders


adders = gen(eval(input()))
print(adders[0](10))
