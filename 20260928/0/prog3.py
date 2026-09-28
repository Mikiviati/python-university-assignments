l = []
while i := input():
    l.append(i)
print(l[-2:len(l) // 2 - 1: -2])
