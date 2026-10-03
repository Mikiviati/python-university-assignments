import sys
data = sys.stdin.read().strip().split('\n')
tmp = [list(map(int, line.split(','))) for line in data]
n = len(tmp[0])

matrix_left = tmp[:n]
matrix_right = tmp[n:]
for i in range(n):
    for j in range(n):
        lc = 0
        for k in range(n):
            lc += matrix_left[i][k] * matrix_right[k][j]
        print(lc, end=',' if j < n - 1 else '\n')
