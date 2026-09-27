res = 0
while (i := int(input())) and i > 0:
    res += i
    if res > 21:
        print(res)
        break
else:
    print(i)
