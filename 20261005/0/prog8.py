
def gen(n):
    adders = []
    for i in range(n):
        adders.append(lambda x, i=i: x + i)
    return adders


adders = gen(eval(input()))
print(adders[0](10))
