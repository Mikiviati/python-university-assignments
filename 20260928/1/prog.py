m, n = map(int, input().split(","))
print([i for i in range(m, n) if all(i % j for j in range(2, i))])
