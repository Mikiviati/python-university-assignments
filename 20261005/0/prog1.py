def average(*args):
    if not args:
        return None
    return sum(args) / len(args)
print(average(*eval(input())))
