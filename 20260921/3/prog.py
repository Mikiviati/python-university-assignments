TABLE_SIZE = 3
n = int(input())
i = 0
while n > 0 and i < TABLE_SIZE:
    j = 0
    while j < TABLE_SIZE:
        mul_cp = mul = (n + i) * (n + j) 
        mul_sum = 0
        while mul_cp > 0:
            mul_sum += mul_cp % 10
            mul_cp //= 10

        print(n + i, "*", n + j, "=", ":=)" if mul_sum == 6 else mul, end=" " if j < TABLE_SIZE - 1 else "\n")
        j += 1
    i += 1
