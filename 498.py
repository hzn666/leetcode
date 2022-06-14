from typing import List


def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    m = len(mat)
    n = len(mat[0])
    dirs = [[-1, 1], [1, -1]]
    dirindex = 0
    row = 0
    col = 0

    result = []

    for i in range(m * n):
        result.append(mat[row][col])
        dir = dirs[dirindex]
        temp_row = row + dir[0]
        temp_col = col + dir[1]

        if temp_row < 0 or temp_row >= m:
            if col < n - 1:
                col += 1
            else:
                # 上行对角线
                row += 1
            dirindex = (dirindex + 1) % 2
        elif temp_col < 0 or temp_col >= n:
            if row < m - 1:
                row += 1
            else:
                # 下行对角线
                col += 1
            dirindex = (dirindex + 1) % 2
        else:
            row = temp_row
            col = temp_col

    return result


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findDiagonalOrder(mat))
