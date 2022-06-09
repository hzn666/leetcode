from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    row, col = 0, 0
    dirindex = 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nums = []

    m, n = len(matrix), len(matrix[0])

    for i in range(m * n):
        nums.append(matrix[row][col])
        matrix[row][col] = "-"
        dx, dy = dirs[dirindex]
        temp_row, temp_col = row + dx, col + dy
        if temp_row < 0 or temp_row >= m or temp_col < 0 or temp_col >= n or matrix[temp_row][temp_col] == "-":
            dirindex = (dirindex + 1) % 4
        dx, dy = dirs[dirindex]
        row, col = row + dx, col + dy
    return nums


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
