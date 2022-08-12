row1 = int(input())
col1 = row2 = int(input())
col2 = int(input())

matrix1 = []
matrix2 = []
res = [[0] * col2 for _ in range(row1)]

for i in range(row1):
    matrix1.append(list(map(int, input().split())))
for i in range(row2):
    matrix2.append(list(map(int, input().split())))

for i in range(row1):
    for j in range(col2):
        for k in range(col1):
            res[i][j] += matrix1[i][k] * matrix2[k][j]

for i in res:
    print(*i)
