l = []
while s := input():
    l.append(int(s))
for i in l:
    if i % 2:
        print(i)
        break
else:
    print(l[0])
