matrix = []
while row := list(map(int, input().split())):
    matrix.append(row)
if not all(len(row) == len(matrix) for row in matrix):
    print("Matrix must be squared")
else:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        print(*row)
