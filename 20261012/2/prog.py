from math import *
import math

data = input().split(maxsplit=4)

W = int(data[0])
H = int(data[1])
A = float(data[2])
B = float(data[3])
f = data[4]

y_values = []

for i in range(W):
    if W == 1:
        x = A
    else:
        x = A + (B - A) * i / (W - 1)

    y = eval(f)
    y_values.append(y)

y_min = min(y_values)
y_max = max(y_values)

screen = [[" " for i in range(W)] for j in range(H)]

prev = None

for i in range(W):
    y = y_values[i]

    if y_max == y_min:
        row = H // 2
    else:
        row = round((y_max - y) / (y_max - y_min) * (H - 1))

    screen[row][i] = "*"

    if prev is not None:
        for j in range(min(prev, row), max(prev, row) + 1):
            if j != prev:
                screen[j][i] = "*"

    prev = row

for line in screen:
    print("".join(line))
