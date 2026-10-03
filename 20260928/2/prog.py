lst = list((int(i), int(i) ** 2 % 100) for i in input().split(","))
for i in range(len(lst), 1, -1):
    done = True
    for j in range(0, i - 1):
        if lst[j][1] > lst[j + 1][1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            done = False
    if done:
        break
print(list(i[0] for i in lst))
