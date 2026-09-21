while n := input():
    match int(n):
        case "1":
            print("one")
        case "2":
            print("two")
        case "3":
            print("three")
        case v if v % 2 == 0:
            print(v, " is even")
        case odd:
            print(odd, "n is too many")
