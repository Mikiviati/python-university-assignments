def div(a, b, eps):
    if abs(b) < eps:
        raise ZeroDivisionError

    return a / b


try:
    print(div(1, 2, 3))
except ZeroDivisionError:
    print("Error!")

