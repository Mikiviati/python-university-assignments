from math import *

functions = {}
lines_count = 0

while line := input():
    lines_count += 1
    if line.startswith(":"):
        name, *args, expr = line[1:].split()

        func = eval(f"lambda  {','.join(args)}: {expr}")

        functions[name] = (func, len(args))
    else:
        name, _, consts = line.partition(" ")
        if name == "quit":
            print(eval(consts).format(len(functions) + 1, lines_count))
            break
        else:

            func, n = functions[name]
            if n == 0:
                arguments = []
            elif n == 1:
                arguments = [eval(consts)]
            else:
                arguments = [eval(a) for a in consts.split()]

            print(func(*arguments))



