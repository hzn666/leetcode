from typing import List


class Solution:
    def isValue(self, board, x, y):
        # 检查已经填入的坐标是否和列中有的元素相等
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        # 检查已经填入的坐标是否和行中有的元素相等
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        # 检查每个正方形是否符合（粗线框内只有1~9）
        m, n = 3 * (x // 3), 3 * (y // 3)  # 这里求出的是3x3网格的左上角的坐标
        for i in range(3):
            for j in range(3):
                if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                    return False

        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValue(board, i, j) and self.solveSudoku(board):
                            return True
                        board[i][j] = '.'
                    return False

        return board
