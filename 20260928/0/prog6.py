a, b = eval(input())
result = [i for i in range(a, b + 1) if i % 2 and "3" not in str(i)]
print(*result)
