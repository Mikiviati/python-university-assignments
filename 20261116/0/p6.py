def itemget(collection, index):
    return collection[index]


def safeindex(fun, *args):
    try:
        return fun(*args)
    except IndexError:
        return None


print([safeindex(itemget, "qwe", i) for i in range(5)])
print(safeindex(itemget, "qwe", "qwe"))
