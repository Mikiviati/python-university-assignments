while i := input():
    if int(i) == 13:
        print("you've typed 13 Bad choise(=")
        break
    if int(i) % 2 == 0:
        print(i)
else:
    print("No 13")
