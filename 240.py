from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0

        while i >= 0 and j < len(matrix[0]):
            if target > matrix[i][j]:
                j += 1
            elif target < matrix[i][j]:
                i -= 1
            else:
                return True
        return False
