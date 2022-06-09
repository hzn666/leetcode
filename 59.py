from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    # 创建矩阵
    matrix = [[0] * n for _ in range(n)]

    # 规定顺时针的四个方向
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirindex = 0
    row, col = 0, 0
    for i in range(n * n):
        print(matrix)
        matrix[row][col] = i + 1
        dx, dy = dirs[dirindex]
        temp_row, temp_col = row + dx, col + dy
        if temp_row < 0 or temp_row >= n or temp_col < 0 or temp_col >= n or matrix[temp_row][temp_col] > 0:
            dirindex = (dirindex + 1) % 4
        dx, dy = dirs[dirindex]
        row, col = row + dx, col + dy
    return matrix


n = 3
print(generateMatrix(n))
