a, b = eval(input())
hw, bw = len(hex(b)), len(bin(b))

for i in range(a, b):
    print(f"{bin(i):{bw}} = {hex(i):>{hw}}")
