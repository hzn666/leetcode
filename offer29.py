from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    row, col = 0, 0
    dirindex = 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nums = []

    m = len(matrix)
    if m <= 0:
        return nums
    n = len(matrix[0])
    print(m,n)

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

matrix = [[0,0,0,3,3,3,1,3,4,5,7,2,2,0,11,7,13,16,10,1,8,19,11,6,6,4,0,23,10,10,29,7,32,5,16,19,24,20,37,21,20,31,29,18,40,15,24,31,4,49,10,36,39,44,42,29,32,43,9,59,54,29,37,56,5,55,20,65,31,59,4,45,49,26,8,61,60,49,52,24,48,31,24,39,59,53,27,49,79,18,56,78,71,35,7,72,30,76,56,39],[0,0,2,2,2,1,0,3,7,6,5,1,4,2,1,6,9,13,10,9,11,2,3,12,15,12,25,7,22,18,9,17,30,33,15,17,12,9,0,38,18,24,24,27,20,9,2,14,7,38,37,12,8,52,16,14,56,19,22,44,47,3,52,38,10,43,26,57,59,35,65,5,66,39,33,22,11,20,10,68,35,52,31,48,3,44,13,83,9,7,48,14,55,47,0,35,28,7,81,63],[0,0,1,3,0,1,6,2,5,9,2,5,5,3,12,11,4,2,0,12,10,21,8,13,5,1,5,5,15,13,21,17,18,5,29,13,2,7,1,13,26,16,35,26,24,40,14,46,20,35,32,44,31,6,16,42,11,24,43,41,41,9,58,42,46,55,16,53,42,4,23,36,21,2,44,4,20,42,4,4,37,18,10,68,73,58,73,77,31,7,33,64,15,82,41,65,78,49,87,11],[0,1,0,1,0,0,5,0,3,9,8,6,0,2,11,15,3,11,12,4,15,6,18,2,1,5,24,10,16,13,8,27,15,28,0,20,2,25,8,15,26,24,9,38,34,38,17,15,5,24,7,24,38,38,36,11,5,12,39,17,39,34,24,5,5,55,20,32,14,46,1,52,48,37,59,49,0,61,54,30,39,0,34,3,77,32,85,10,21,3,39,8,71,6,86,50,20,26,24,28],[0,0,0,0,0,1,1,3,2,2,0,2,8,6,12,13,8,6,18,6,12,10,15,8,24,5,14,25,15,8,7,16,7,22,1,0,22,33,17,3,37,24,37,32,37,6,23,7,16,23,43,51,15,28,35,33,38,9,8,5,22,33,24,57,33,35,38,58,42,15,64,16,9,69,45,38,19,41,41,35,3,80,74,48,46,4,73,30,81,42,51,37,88,84,19,95,71,83,87,82],[0,0,0,2,2,0,6,5,3,6,2,10,0,12,12,0,14,11,8,10,18,7,11,4,10,7,26,16,20,24,5,8,30,1,25,23,15,16,5,25,12,13,38,18,7,23,41,20,25,49,41,49,40,47,2,9,7,9,14,14,25,5,10,56,16,63,34,32,64,19,18,9,41,38,55,43,55,6,71,5,7,16,81,47,55,69,11,26,70,78,38,21,52,82,65,79,32,39,64,65],[0,0,0,2,1,0,1,7,7,4,1,4,0,7,4,15,0,7,6,2,3,16,6,20,14,18,12,10,27,16,4,14,4,4,11,29,0,15,28,15,6,24,3,30,11,26,43,22,28,47,33,12,17,20,47,5,10,2,12,32,21,52,12,14,18,19,24,2,29,50,68,24,34,51,31,18,59,40,67,6,28,3,2,54,6,79,4,28,1,84,17,4,0,4,50,82,18,4,74,75],[0,1,1,3,2,1,6,4,0,8,5,4,0,6,7,4,9,5,9,1,13,19,17,0,7,16,15,24,1,4,18,8,24,9,18,31,18,36,0,4,24,15,12,23,15,7,25,41,26,28,23,30,4,53,14,39,25,12,9,13,10,57,10,23,2,9,42,41,41,49,58,21,40,65,1,74,72,45,77,9,63,75,40,13,35,64,81,6,73,23,51,62,28,0,89,52,54,60,56,26],[0,0,0,2,3,0,6,7,8,3,3,10,8,4,11,9,1,9,18,17,9,12,13,22,1,6,17,20,24,14,26,5,18,15,9,24,28,33,11,11,21,36,24,5,38,15,25,9,43,8,44,50,20,52,26,54,5,52,21,46,35,6,59,25,5,33,58,37,49,62,44,46,28,69,19,20,68,7,42,67,20,32,56,55,3,7,28,85,33,4,37,22,6,16,48,87,62,46,72,8],[0,0,1,3,0,3,3,2,3,4,1,9,9,9,0,15,4,15,16,18,16,18,1,2,11,17,2,15,11,23,30,5,26,29,4,11,33,29,19,17,3,32,4,42,18,29,32,8,0,1,46,20,10,23,52,11,23,55,20,3,26,45,43,33,1,18,1,3,39,41,8,37,43,13,3,8,58,51,46,26,48,14,36,10,26,15,0,25,16,49,68,1,42,74,31,36,3,22,24,19],[0,1,2,3,1,4,0,2,0,3,0,7,7,4,14,14,2,15,5,19,11,4,16,18,5,16,5,5,7,17,7,10,18,22,5,29,34,36,20,37,24,6,2,36,23,37,13,22,5,21,34,38,26,26,26,37,24,8,25,6,5,54,25,18,15,63,18,19,28,29,10,25,22,46,61,54,5,44,58,55,22,10,32,56,66,82,64,67,75,81,83,50,90,35,43,39,90,73,6,13],[0,1,1,1,4,3,6,1,2,5,6,11,3,3,14,10,7,9,4,13,15,5,0,3,22,6,16,4,21,0,10,4,9,12,34,25,29,37,16,13,34,2,41,20,39,42,2,27,8,17,49,49,8,3,18,2,3,47,56,45,38,13,41,2,4,16,50,21,32,15,34,16,47,25,49,46,48,48,29,20,47,4,13,31,50,83,41,55,56,39,48,59,9,6,55,23,47,48,56,92],[0,0,2,1,2,4,5,3,0,3,7,11,2,1,10,12,6,5,13,10,7,0,5,1,7,18,0,0,6,5,9,25,20,26,15,23,0,37,25,12,10,8,6,10,14,40,7,13,33,40,18,6,24,48,47,4,46,26,30,35,32,47,17,34,36,60,21,19,1,65,47,44,44,28,44,45,33,76,32,49,48,56,1,71,48,50,15,86,86,27,25,81,30,85,49,91,57,37,14,34],[0,1,0,0,0,0,3,0,6,2,3,6,5,9,1,13,6,3,0,11,16,12,19,15,15,18,4,22,24,6,5,26,23,7,8,3,32,7,28,39,7,30,41,4,37,16,40,29,24,41,24,11,51,37,10,40,1,46,18,23,37,6,35,18,49,64,40,8,7,32,38,30,13,9,45,34,57,36,2,71,80,81,66,51,73,58,48,48,81,77,2,59,9,76,54,35,18,5,24,68],[0,1,1,1,1,1,6,7,4,6,5,3,0,2,7,8,13,17,15,2,0,2,5,3,19,13,11,27,19,7,16,29,20,6,15,26,24,23,27,4,27,26,36,33,10,28,34,27,37,37,4,33,12,0,50,34,45,14,36,1,9,57,18,20,43,47,27,42,57,47,58,35,5,21,32,73,21,68,75,14,14,60,4,12,37,72,66,3,88,72,34,69,58,61,30,6,88,77,21,96],[0,0,0,2,2,3,4,7,2,7,2,10,1,13,2,13,15,5,7,16,20,12,7,18,3,6,6,1,21,21,1,7,32,10,17,15,13,18,37,11,16,10,3,7,26,27,33,44,8,44,1,22,44,51,12,21,25,20,18,12,30,41,62,21,3,3,2,58,50,17,66,59,39,19,55,38,35,29,59,33,76,66,79,14,47,46,43,36,80,60,35,38,82,17,42,92,58,38,47,9],[0,0,0,3,3,0,3,0,5,3,6,6,8,2,2,7,12,8,14,1,4,6,15,16,1,16,21,5,18,26,13,1,18,26,31,13,9,13,13,23,19,35,20,9,3,34,12,22,8,17,13,51,26,39,8,46,51,3,4,36,28,41,36,18,54,11,66,6,10,26,31,46,26,37,59,54,42,10,42,18,10,39,37,44,2,75,36,15,80,26,11,7,85,23,91,6,33,83,69,92],[0,0,1,0,1,2,3,2,5,3,8,8,12,1,10,12,13,16,2,0,15,17,9,11,1,9,3,1,4,21,24,27,6,27,12,10,14,0,27,36,32,13,22,12,13,28,11,24,44,17,18,50,52,14,28,52,40,30,13,0,43,49,6,4,24,49,61,36,51,45,10,1,62,17,39,65,37,63,49,40,3,48,73,50,78,79,52,40,6,6,35,87,56,7,77,33,62,43,9,72],[0,0,0,1,3,2,1,0,8,7,10,4,5,10,13,10,7,3,11,0,11,17,19,21,23,6,23,10,12,27,25,3,25,30,13,13,17,24,8,38,2,32,6,11,5,4,20,40,31,43,11,38,19,9,5,49,54,17,9,35,40,48,45,51,21,45,29,17,40,53,61,50,14,31,19,60,18,73,28,44,79,65,30,74,75,14,13,48,12,73,64,67,43,26,30,61,55,25,44,74],[0,0,1,0,3,1,6,0,5,5,6,5,4,9,7,1,16,16,17,16,18,9,11,8,11,18,2,7,20,27,6,19,5,23,3,3,2,1,36,3,24,1,42,15,7,28,35,31,26,35,6,21,42,22,39,3,30,57,4,14,51,53,10,16,18,57,47,22,31,12,6,12,61,66,64,12,5,15,33,69,41,2,70,66,78,39,28,18,60,35,80,5,33,48,30,0,65,8,91,1],[0,0,2,0,4,4,0,5,8,3,4,9,8,4,4,13,13,6,13,1,19,1,15,16,16,6,3,0,13,5,6,31,2,7,23,9,33,2,23,34,30,9,5,35,39,13,0,42,16,25,20,23,7,20,46,34,5,32,1,35,25,35,10,20,5,36,44,21,2,58,24,30,12,21,21,62,30,0,68,56,57,59,78,34,54,16,59,63,21,43,56,56,27,58,92,49,52,38,14,4],[0,0,2,1,2,1,5,6,7,1,0,4,8,13,7,12,5,13,5,9,1,9,14,18,6,18,12,19,17,7,10,21,18,20,33,11,20,37,32,19,39,30,21,41,2,22,45,40,35,10,2,16,40,30,13,1,48,34,54,21,15,54,24,52,49,6,62,7,5,49,57,6,32,14,55,17,0,62,61,63,58,38,78,76,27,70,54,1,75,23,33,60,22,51,9,89,50,59,96,57],[0,0,1,2,0,0,6,5,6,1,8,7,4,0,5,0,6,0,0,11,5,9,12,9,22,6,12,26,24,20,23,27,13,22,26,4,10,4,17,16,35,34,11,40,35,31,28,14,2,0,18,31,10,17,25,30,20,50,24,27,9,58,24,5,20,22,24,21,20,51,31,49,2,37,39,49,3,71,63,78,38,34,58,82,24,73,83,75,0,20,59,30,83,12,47,64,4,25,54,31],[0,1,1,3,3,2,3,2,2,9,0,9,5,4,8,2,6,7,14,17,16,15,21,0,13,4,25,27,28,17,10,0,13,3,16,15,35,27,8,3,24,7,30,25,34,12,39,1,22,16,14,22,29,41,3,19,55,3,1,40,42,51,35,14,6,58,28,17,9,28,22,16,31,3,66,68,1,57,19,9,12,21,67,18,37,85,62,14,18,79,85,83,7,1,12,44,36,6,60,35],[0,1,1,1,1,5,3,2,0,3,8,2,1,9,10,15,5,9,9,12,19,21,22,18,24,2,0,5,3,1,6,18,0,16,10,21,7,27,33,8,27,21,30,22,12,16,9,35,37,25,44,39,8,39,24,18,43,3,18,26,25,49,32,22,42,58,35,17,21,8,4,46,56,0,30,41,19,3,1,30,8,12,57,48,76,29,63,10,78,47,51,38,72,15,66,79,84,92,29,51],[0,0,0,1,2,5,4,0,7,9,10,8,7,10,13,7,11,10,13,14,16,0,7,12,1,25,20,20,20,7,3,0,15,9,24,9,27,19,1,1,37,31,38,20,0,43,39,32,46,18,13,31,8,43,31,22,43,10,11,19,27,8,48,51,59,12,4,55,25,4,32,25,11,6,35,22,63,64,53,48,60,45,72,68,4,66,79,82,73,80,23,28,86,4,68,81,87,94,83,70],[0,0,0,3,1,3,1,7,8,8,1,4,4,0,3,10,6,17,12,1,20,7,9,10,6,1,18,11,27,25,14,21,21,20,28,6,14,7,33,28,15,23,3,2,36,23,29,47,4,8,19,17,25,17,7,37,42,2,7,45,22,61,13,54,36,10,22,28,53,4,24,37,23,45,13,12,29,53,58,45,11,24,56,54,40,1,5,11,63,54,30,1,48,72,77,51,82,0,79,98],[0,1,1,3,3,5,3,3,7,6,1,11,12,7,7,2,15,0,5,12,20,10,13,2,3,18,1,14,9,4,1,9,31,6,9,0,11,29,8,16,23,5,28,34,17,40,9,46,5,38,48,46,43,15,14,43,14,42,1,55,57,5,34,37,4,21,42,9,12,46,12,64,53,7,15,3,0,38,74,71,3,30,15,36,33,49,40,9,4,64,10,32,29,83,81,28,62,54,28,55],[0,1,1,2,4,4,1,2,5,7,2,8,10,13,8,4,15,12,6,18,6,21,4,5,14,6,17,3,2,20,25,27,22,15,6,15,7,22,33,35,33,25,11,32,38,40,4,5,9,2,19,51,39,42,32,16,19,28,13,21,14,41,62,4,18,5,41,55,37,23,59,40,67,45,73,62,76,29,26,33,35,56,53,79,37,20,36,14,35,78,30,81,8,50,17,69,17,54,90,46],[0,0,1,0,2,4,4,7,5,3,6,9,10,0,5,8,0,6,2,14,19,7,16,1,17,24,23,21,7,15,1,19,30,0,7,10,2,19,36,24,7,40,13,9,1,31,22,26,46,41,21,31,1,37,51,25,39,35,1,10,45,1,18,46,12,27,43,28,4,1,8,49,21,6,13,72,9,74,58,64,62,41,21,14,40,17,19,45,1,47,9,45,16,85,32,16,74,80,86,83],[0,0,0,2,3,3,6,3,4,0,0,1,12,10,0,11,9,10,8,19,13,10,5,13,14,22,25,16,6,24,29,13,21,30,20,33,18,20,17,37,23,37,16,24,24,2,21,3,1,23,23,11,36,5,40,13,31,33,51,54,20,44,58,18,52,41,61,31,38,30,0,37,44,28,35,19,55,8,71,72,53,55,34,82,78,56,70,56,31,58,76,78,7,85,7,78,53,66,77,55],[0,1,0,1,0,4,2,0,8,9,3,6,9,5,10,11,11,12,15,9,6,1,9,8,10,17,26,23,27,10,30,3,0,11,10,3,0,28,35,14,4,0,31,0,37,13,25,35,48,14,37,13,48,3,12,39,20,30,48,25,15,41,60,37,7,44,53,42,25,58,27,17,8,59,27,67,15,54,17,44,50,62,36,47,33,20,42,59,8,61,24,42,45,79,0,28,59,22,59,8],[0,1,0,2,1,4,2,6,1,4,5,6,8,13,9,14,11,13,14,2,12,11,11,18,7,4,0,12,3,17,0,18,15,33,6,21,16,36,7,19,24,31,3,4,15,21,18,14,30,49,21,0,25,15,8,14,56,37,44,43,43,49,44,33,12,33,57,63,21,10,24,33,51,35,2,55,64,0,42,26,72,74,19,9,84,23,38,9,88,65,52,38,61,19,27,59,67,79,31,64],[0,0,2,2,4,3,5,1,7,8,6,1,5,0,3,6,2,10,15,12,7,13,20,0,14,13,24,16,14,17,2,21,20,19,4,0,1,16,0,20,7,18,32,29,9,28,19,44,4,47,14,45,18,47,38,41,16,23,42,36,5,55,20,1,41,16,26,24,62,7,42,25,23,52,5,41,37,45,73,19,36,60,30,56,58,22,68,17,62,21,48,86,72,62,77,87,40,41,58,61],[0,1,0,0,0,4,2,5,2,3,7,7,5,6,7,8,13,15,13,14,16,6,8,15,15,3,3,5,18,2,9,9,15,33,11,1,7,17,7,7,0,6,2,41,17,38,28,40,48,22,40,18,13,34,11,1,34,25,45,17,29,24,17,29,2,60,21,24,67,28,3,39,67,45,25,50,43,18,21,43,54,72,15,33,19,37,42,8,0,24,81,15,1,10,26,70,19,25,42,22],[0,1,2,1,0,1,4,1,8,5,0,0,4,11,1,2,16,14,1,17,11,20,3,10,21,23,14,12,2,10,27,21,11,14,9,35,8,19,20,4,24,37,23,24,2,31,11,8,2,14,5,45,24,28,36,5,44,10,5,1,9,42,10,11,30,3,46,13,54,67,55,70,23,22,71,29,18,42,39,39,42,15,75,4,4,66,80,62,55,56,51,40,74,28,7,13,75,68,79,70],[0,1,1,1,0,5,3,0,7,5,0,1,9,9,2,3,14,12,10,0,10,10,13,13,22,18,3,14,4,8,1,17,10,14,31,6,17,25,28,21,19,41,32,13,15,7,30,25,37,37,33,25,30,38,21,34,19,43,3,17,39,44,43,41,5,31,34,63,28,51,32,71,43,23,35,41,27,56,5,24,30,66,32,16,8,69,33,71,62,68,34,76,78,89,91,48,39,95,19,18],[0,1,1,2,2,5,5,6,4,1,0,4,2,9,5,12,3,11,3,8,9,15,4,15,15,7,17,23,9,19,16,25,15,18,33,29,2,9,28,20,3,41,40,35,40,18,13,45,8,21,40,31,10,39,31,36,2,46,23,58,48,52,39,52,12,43,21,37,49,57,13,41,71,1,46,70,34,23,52,62,66,44,35,37,55,8,65,56,84,18,76,88,52,18,17,88,31,86,25,63],[0,0,0,2,4,3,6,3,5,1,5,9,11,0,5,4,7,12,10,4,18,4,19,1,23,22,1,15,26,9,14,0,12,6,10,9,1,10,13,7,14,37,11,42,17,26,33,0,0,24,4,35,51,18,28,43,23,12,28,36,1,14,1,60,43,59,32,34,5,60,32,68,11,36,5,56,66,75,44,26,23,21,36,24,55,8,32,40,58,62,76,90,13,52,22,43,94,70,11,54],[0,0,1,0,3,5,2,2,8,1,2,2,2,9,8,5,6,7,17,9,15,8,8,17,5,9,10,27,17,11,28,17,20,7,18,18,36,23,23,21,32,6,35,27,5,19,12,25,39,6,2,51,19,23,48,3,15,7,18,57,17,3,14,19,39,25,40,43,7,21,18,38,23,21,2,35,25,32,76,22,12,26,77,78,56,83,81,6,2,34,51,60,86,63,66,75,3,3,56,34],[0,1,0,0,1,1,1,3,2,8,0,10,12,6,7,4,5,14,5,7,9,21,8,6,3,9,11,20,5,27,16,8,13,13,34,24,29,14,30,34,19,18,8,42,6,4,32,15,17,24,11,49,8,3,20,50,47,55,10,37,36,31,54,50,39,53,48,35,65,58,45,64,2,34,38,37,34,47,3,29,30,47,53,27,41,46,80,1,0,9,52,90,14,60,59,75,54,25,88,76],[0,0,2,2,0,2,2,1,4,9,1,8,3,11,2,2,13,5,16,16,17,9,8,17,15,17,6,7,16,21,8,5,5,25,6,3,33,5,19,11,31,27,3,30,2,11,4,1,38,27,0,47,47,4,38,4,48,16,40,14,38,20,24,30,8,17,8,57,46,23,62,57,36,73,73,21,63,3,38,18,13,66,55,32,11,56,23,37,6,40,88,30,37,22,41,64,18,34,97,24],[0,1,2,0,3,3,4,7,5,2,2,11,4,12,14,14,14,0,14,11,14,19,5,9,23,8,18,20,15,1,8,31,31,2,24,9,29,19,35,10,4,33,27,29,3,19,28,13,0,30,15,29,44,27,31,17,35,29,54,18,36,0,21,35,53,21,52,49,48,20,37,67,34,64,62,44,39,45,76,70,31,4,31,70,67,21,66,49,7,45,69,64,64,2,47,11,53,41,0,17],[0,1,1,1,4,0,4,6,2,8,3,8,6,3,9,15,9,2,9,11,7,6,11,4,1,18,26,4,10,6,12,10,24,13,32,21,17,30,18,28,12,27,15,10,13,8,7,5,28,42,23,24,10,37,1,19,14,51,32,31,24,6,33,0,1,55,66,55,40,34,16,52,59,63,51,5,24,46,46,13,47,41,28,35,27,34,53,79,79,55,87,90,46,50,21,76,76,77,37,89],[0,0,0,1,1,5,1,2,0,8,6,6,7,2,4,8,4,5,4,19,4,11,9,7,15,2,7,1,27,5,3,20,3,6,20,33,25,30,28,23,24,9,23,40,42,5,2,10,43,9,7,11,7,17,0,52,21,1,55,12,34,39,20,37,11,20,8,41,25,8,26,51,8,71,71,59,18,1,51,64,48,79,74,19,68,8,81,84,14,43,9,1,85,64,84,65,44,26,23,21],[0,1,0,0,3,5,6,3,7,8,3,4,2,2,13,11,13,6,3,16,1,12,9,7,15,1,22,14,23,22,20,8,28,8,31,20,6,23,17,26,32,28,36,42,18,33,10,5,21,48,19,21,12,10,43,51,15,7,53,40,40,37,35,23,27,29,2,17,37,20,36,55,64,25,58,73,8,39,76,45,46,77,44,39,48,10,56,70,60,76,7,14,1,91,18,28,11,28,65,27],[0,1,0,2,3,3,0,6,4,9,6,10,5,5,8,6,5,4,15,1,18,6,20,11,21,8,0,15,6,3,24,7,30,20,14,17,7,15,0,15,6,12,39,3,36,5,41,21,30,32,23,15,5,48,39,18,45,4,13,52,17,16,11,22,32,43,34,12,19,27,20,13,34,54,62,4,54,46,34,62,59,30,28,22,77,80,11,84,1,51,83,60,33,30,26,80,82,66,31,79],[0,0,2,2,3,2,0,6,6,9,2,8,0,13,13,0,6,2,1,19,20,2,13,12,17,13,21,0,12,20,24,3,10,23,34,28,25,2,6,9,9,22,23,31,4,15,28,34,4,1,37,3,11,50,16,41,22,32,32,50,30,51,47,45,1,25,55,3,68,39,69,45,47,58,3,66,1,8,60,23,38,31,40,35,77,61,22,2,75,42,57,21,59,20,1,81,94,55,12,46],[0,0,0,2,3,3,4,5,1,6,8,4,9,2,12,13,5,12,11,9,2,1,13,6,7,8,5,11,12,7,16,3,21,14,15,2,33,32,11,36,2,41,13,17,16,18,13,13,22,44,46,14,31,7,34,20,18,32,42,7,52,23,53,58,10,38,48,54,17,25,14,8,67,18,54,55,74,55,25,45,42,6,44,52,18,66,18,85,65,84,3,47,64,10,57,86,21,43,6,11],[0,0,1,3,0,2,0,4,0,0,6,3,5,10,0,3,1,0,16,17,7,17,4,4,9,19,25,3,19,15,7,14,30,1,1,12,32,33,5,10,9,36,27,4,3,21,0,20,34,23,43,38,30,42,34,46,4,18,15,53,30,60,21,0,63,29,20,3,22,59,7,15,57,5,17,35,26,63,13,1,74,25,36,29,8,13,43,41,58,7,42,47,55,92,86,7,16,11,4,95],[0,0,0,3,2,3,2,4,4,3,7,5,8,0,8,0,0,13,6,3,12,12,8,19,16,1,1,16,10,26,27,24,29,11,29,15,8,4,8,19,11,16,11,31,40,24,34,19,21,45,17,14,36,7,30,48,38,35,16,23,49,31,6,50,43,42,3,4,17,64,59,24,38,3,18,56,17,30,19,29,68,24,71,80,76,39,50,13,39,68,16,17,3,32,56,28,33,73,91,69],[0,0,0,1,2,4,3,7,3,0,6,3,3,2,9,12,10,12,7,18,7,6,6,5,19,0,6,7,0,4,13,21,26,14,31,27,22,12,2,10,24,34,0,39,10,29,19,46,21,44,33,23,10,26,1,16,9,4,50,9,60,11,18,63,25,33,66,56,63,62,46,68,2,17,3,18,36,21,62,25,18,45,57,68,38,50,58,66,26,11,55,70,45,52,84,43,41,28,94,52],[0,1,2,2,3,5,3,5,5,0,7,6,1,4,12,10,8,17,18,7,0,18,13,5,7,11,11,16,16,12,22,29,4,23,29,9,3,22,22,27,12,0,38,29,38,45,37,9,11,23,38,47,2,53,20,18,51,6,44,57,0,54,21,54,19,23,46,34,17,69,35,6,22,16,20,29,30,24,74,24,10,22,56,21,77,50,13,55,64,62,78,7,45,74,2,37,61,13,36,4],[0,0,0,1,2,4,4,5,0,0,0,4,6,4,9,0,1,16,13,14,7,11,17,17,18,18,0,4,3,11,17,3,18,25,18,31,1,34,37,2,24,18,19,13,31,34,41,11,34,33,26,18,46,46,47,40,34,24,50,32,56,17,51,59,14,48,0,58,2,35,29,12,55,72,52,31,17,8,47,53,4,60,42,44,19,25,61,64,72,27,52,18,16,65,38,94,77,48,53,83],[0,1,2,1,0,0,5,3,3,2,4,8,1,7,4,12,7,13,5,6,1,15,11,0,24,12,3,23,12,4,24,16,1,5,9,8,6,21,22,37,21,5,12,29,1,36,13,34,9,28,6,1,2,21,32,18,56,21,20,3,3,30,49,18,62,50,53,14,26,6,3,25,4,65,39,23,52,42,37,40,75,16,67,31,1,51,55,44,22,74,25,41,34,40,40,25,18,11,10,9],[0,0,1,3,2,4,4,3,0,9,10,5,0,9,0,14,3,16,12,15,16,14,1,14,15,25,25,0,12,25,20,17,6,23,10,30,24,14,4,36,8,37,11,42,40,35,9,21,31,23,10,23,36,36,1,35,37,5,55,55,0,43,34,40,17,3,22,56,13,37,37,47,19,17,0,71,13,72,35,76,62,70,35,53,3,39,74,84,62,13,76,80,8,85,40,13,50,17,13,91],[0,1,2,2,4,2,0,4,7,8,8,1,4,2,10,7,15,15,7,11,4,9,21,10,12,3,16,9,4,11,27,12,12,12,32,10,1,5,34,30,25,3,11,7,8,24,28,8,42,15,0,17,23,5,45,54,24,43,41,35,8,34,4,50,62,49,42,2,51,41,2,48,24,42,40,71,9,6,7,46,72,26,14,29,43,23,39,4,73,57,52,13,8,54,53,44,23,21,86,95],[0,0,1,1,0,3,4,3,2,9,0,4,5,0,9,15,6,1,7,10,18,12,1,13,19,3,12,8,21,7,27,2,10,9,12,27,36,21,8,3,0,3,36,42,8,0,46,17,20,42,7,41,9,43,32,27,42,56,16,59,42,30,23,8,57,57,48,61,25,66,31,58,69,27,40,47,16,70,15,64,33,27,44,29,68,78,40,35,6,27,48,49,74,55,86,36,56,60,86,35],[0,0,1,1,0,0,3,0,0,2,1,8,10,13,11,11,6,10,3,1,20,1,14,6,17,9,16,21,14,5,30,5,10,10,5,13,6,16,29,27,19,33,41,24,18,18,2,33,0,33,21,21,4,50,52,50,36,11,22,55,57,53,18,24,44,23,38,14,63,59,32,54,16,49,54,20,32,77,76,39,10,29,53,30,35,50,78,84,5,83,57,22,67,17,69,6,41,96,6,55],[0,0,2,3,0,2,6,5,0,4,8,8,0,9,13,8,9,14,7,12,11,15,14,11,3,22,10,23,7,0,6,7,0,1,29,29,27,13,37,14,12,18,14,36,0,27,34,11,8,14,43,40,52,47,22,30,29,35,51,4,47,50,4,20,52,33,8,36,11,59,60,21,66,5,68,44,75,0,62,55,29,1,17,20,45,77,29,39,18,25,2,63,15,15,82,24,29,50,93,20],[0,1,1,1,4,5,1,3,8,2,7,6,6,13,3,13,16,2,17,12,14,10,18,4,20,11,5,4,23,27,9,30,5,2,33,11,16,20,36,15,3,40,9,23,3,9,19,31,48,0,11,31,50,44,9,42,20,57,34,23,13,37,23,63,24,48,43,64,26,50,0,31,41,42,30,56,65,20,73,39,75,14,42,40,24,38,59,13,86,84,32,57,43,33,81,32,9,31,27,11],[0,1,0,1,2,5,2,2,1,5,8,7,11,0,10,9,5,6,3,18,16,6,13,20,17,17,22,5,18,28,18,20,23,15,13,27,17,21,30,24,32,0,2,18,10,42,37,15,1,38,16,38,4,25,26,38,29,16,25,48,46,47,13,18,7,47,54,50,1,59,56,63,71,58,12,9,19,62,60,23,46,8,79,71,62,16,18,63,45,15,44,45,51,11,68,40,2,91,9,15],[0,0,0,1,4,0,2,4,1,6,1,9,9,6,7,13,12,12,16,12,13,18,3,17,8,20,21,2,7,2,29,10,7,16,9,10,18,19,19,11,33,40,34,35,15,8,13,22,18,16,20,49,22,47,21,8,47,19,36,37,26,14,34,11,13,62,17,36,66,67,8,17,65,11,38,37,50,19,13,47,14,4,9,2,39,62,30,44,1,86,15,70,44,32,81,0,29,89,50,4],[0,1,1,1,0,0,2,2,7,1,5,1,0,11,9,1,4,4,6,1,3,13,9,22,9,6,4,9,7,13,7,24,6,9,30,34,34,14,17,39,2,8,31,33,26,37,2,22,31,27,2,4,4,8,47,19,11,10,44,19,59,41,54,28,28,51,55,5,36,10,48,21,6,59,40,33,22,32,47,7,4,51,74,9,10,36,78,4,63,0,84,40,72,11,30,14,42,51,41,61],[0,0,2,3,2,4,5,6,1,6,7,9,0,9,9,14,15,13,6,6,18,21,15,17,3,8,24,23,21,27,12,12,9,4,6,0,16,11,14,15,4,11,12,20,7,9,35,29,9,16,4,40,32,42,8,4,4,50,19,16,60,32,56,33,22,54,49,65,65,15,17,64,58,62,2,14,11,31,12,6,52,23,57,2,44,13,29,47,20,76,14,76,22,3,22,26,16,68,93,78],[0,0,2,3,2,3,6,4,2,4,0,6,5,12,1,8,10,6,11,2,13,16,19,13,20,23,4,1,28,18,1,25,17,13,30,26,12,17,25,3,28,12,12,11,19,3,45,42,27,8,20,10,34,27,39,32,2,35,32,57,36,27,13,12,32,47,25,60,41,15,60,49,27,56,12,36,9,15,78,39,70,1,39,38,71,16,16,66,52,21,40,64,50,23,43,26,33,88,18,98],[0,1,0,2,0,1,2,5,0,5,3,1,12,10,5,15,13,1,16,10,7,1,18,22,13,7,17,7,17,1,15,15,10,4,5,19,15,25,19,6,5,28,3,24,2,4,8,37,22,7,0,43,15,52,29,24,44,57,45,16,3,0,7,8,15,54,47,31,30,25,17,18,11,41,26,20,28,9,68,68,34,70,48,52,15,50,79,39,5,71,34,70,10,87,45,1,9,83,20,5],[0,1,0,0,0,1,6,1,4,5,9,6,7,10,5,6,1,8,5,2,2,8,4,9,12,6,0,13,7,7,17,20,8,1,7,33,3,4,5,2,0,27,3,25,3,22,28,27,20,26,31,12,43,35,48,27,40,35,16,23,12,45,60,40,51,51,1,28,30,39,57,24,67,17,72,57,44,29,20,33,5,13,46,31,17,44,40,9,8,28,48,52,49,24,15,64,20,51,69,98],[0,0,0,2,3,4,5,1,2,9,5,4,10,3,2,2,12,11,11,3,5,4,21,21,16,23,22,24,28,27,22,10,8,24,16,15,0,25,34,30,26,9,37,2,18,23,41,3,16,19,45,22,31,17,11,51,17,30,32,41,0,39,45,10,3,0,47,10,9,3,38,43,37,52,57,49,2,43,71,12,76,6,31,0,4,66,43,14,64,89,60,31,49,8,89,44,26,14,22,38],[0,0,0,2,3,3,1,4,1,7,2,5,9,0,2,9,16,15,4,5,17,16,12,5,9,22,6,20,8,17,27,21,20,10,31,26,32,4,29,6,11,12,39,13,40,33,32,36,32,33,36,23,32,50,22,31,4,27,33,52,17,17,46,29,54,37,52,41,56,63,37,16,53,46,45,56,60,5,35,63,67,76,0,0,79,19,69,83,25,41,20,52,20,65,75,21,62,26,86,66],[0,1,0,2,4,3,6,5,7,0,5,0,2,1,3,14,7,14,10,10,16,19,16,4,16,16,26,11,4,1,22,2,23,32,8,27,17,15,8,10,19,21,6,23,36,5,39,45,20,39,14,12,11,30,32,6,17,16,3,2,57,21,53,24,56,15,46,10,39,33,23,9,44,10,18,24,53,24,6,36,30,45,54,36,47,48,3,0,84,44,66,42,68,68,58,89,30,68,63,6],[0,1,2,0,4,0,6,4,7,7,6,1,1,10,3,15,12,12,9,13,15,6,4,14,22,13,24,12,23,25,2,24,1,33,18,1,31,5,31,39,17,5,25,10,34,0,4,35,41,39,49,42,8,37,6,2,42,35,20,14,48,22,26,23,38,30,53,54,53,66,67,1,41,32,56,1,68,40,26,62,50,73,45,77,5,16,72,21,64,30,89,24,72,61,79,20,88,31,45,34],[0,0,0,3,1,0,1,3,8,9,9,2,8,12,8,7,3,9,1,10,6,18,22,18,22,5,18,14,9,22,28,28,18,10,2,32,8,1,4,18,21,39,27,42,31,30,38,43,37,36,1,32,2,2,9,11,52,27,14,1,33,34,1,9,38,53,40,35,23,53,4,54,69,26,28,20,8,4,48,35,36,70,5,71,48,42,31,55,70,63,43,47,38,19,42,8,66,95,22,43],[0,0,2,2,0,1,6,5,2,2,8,11,8,11,9,8,1,14,10,11,10,21,10,5,12,10,12,25,17,23,9,25,21,12,10,32,9,13,28,13,0,26,7,24,29,5,3,27,17,18,17,25,43,42,39,40,11,21,57,53,58,11,20,57,25,61,44,45,64,29,35,37,46,39,1,54,45,39,18,32,51,14,51,60,23,39,57,67,37,51,77,12,37,47,48,32,94,15,87,91],[0,0,2,1,3,1,4,6,3,5,9,4,9,13,0,9,12,17,15,19,4,1,10,12,21,4,4,16,4,3,3,3,4,4,27,16,14,13,12,14,12,17,21,36,12,13,3,33,22,35,49,14,8,9,38,45,17,16,36,40,49,13,12,12,37,63,32,14,17,60,34,36,63,64,68,9,43,13,78,12,57,75,82,47,1,8,10,40,65,16,40,19,22,79,88,94,77,31,13,68],[0,0,1,1,3,3,4,5,8,2,0,2,3,9,13,11,9,11,12,11,17,20,21,4,0,16,19,12,4,15,30,9,14,17,30,20,22,16,27,36,14,27,6,8,9,40,2,25,25,18,33,35,20,33,36,17,1,29,46,36,48,35,2,40,37,9,5,28,41,66,46,59,71,4,5,26,0,21,5,26,41,6,41,18,53,30,10,72,69,80,88,86,68,73,86,54,90,96,5,25],[0,0,2,1,3,4,6,6,0,5,7,0,6,4,11,8,8,15,13,6,11,20,11,21,8,21,15,3,12,6,7,30,27,0,31,25,20,22,36,28,37,30,36,25,2,44,9,30,29,12,10,33,5,24,8,6,32,24,6,3,17,41,23,51,46,46,42,4,16,38,0,12,62,30,46,46,34,60,8,64,23,36,56,62,25,51,27,75,1,5,9,63,79,36,94,95,25,76,96,55],[0,1,2,0,1,1,3,1,4,6,9,3,6,6,13,9,16,2,10,13,10,1,6,14,7,21,17,22,21,19,13,28,22,7,1,27,2,35,22,18,12,22,13,37,44,40,1,46,19,34,49,38,3,21,43,10,33,22,52,24,27,53,23,51,18,9,2,48,52,6,68,6,67,52,40,11,61,14,73,40,37,62,6,42,24,22,28,33,79,28,26,43,35,30,73,39,20,46,61,59],[0,0,2,0,0,3,3,4,0,5,1,2,5,5,12,6,13,5,7,19,12,21,1,6,0,10,25,22,5,13,5,27,19,23,30,9,4,20,13,23,35,30,21,7,34,27,34,11,42,40,46,43,7,27,46,2,21,54,27,41,5,51,17,15,17,26,12,63,40,64,43,69,10,55,15,6,58,45,49,5,43,14,55,29,77,20,67,85,33,46,32,31,29,38,16,5,95,13,36,65],[0,1,2,2,1,3,2,1,6,2,10,7,8,2,9,3,14,5,9,10,4,16,11,23,11,1,4,9,10,13,21,6,27,21,5,3,0,8,10,39,36,37,29,3,39,35,39,2,25,36,49,22,43,30,27,10,22,42,40,9,32,46,60,42,22,54,33,3,7,15,53,10,22,10,61,49,59,29,31,45,70,10,32,25,35,16,42,23,65,76,25,33,64,27,31,52,95,91,74,62],[0,0,2,1,4,2,6,7,8,5,1,3,5,2,13,3,11,7,0,2,11,7,17,22,21,15,12,27,12,29,11,18,24,9,24,17,18,32,28,12,12,33,36,37,7,0,23,7,10,38,32,30,52,32,0,4,10,49,1,49,21,1,54,34,27,26,33,48,17,39,43,19,65,27,2,13,44,29,24,30,64,74,7,54,55,67,28,86,5,2,49,79,7,3,22,19,17,46,90,5],[0,1,0,3,4,5,3,1,1,4,5,11,12,9,5,8,15,11,14,5,0,3,4,0,6,15,1,16,27,24,11,31,23,30,31,0,31,8,6,28,39,29,38,3,29,13,18,21,5,21,30,50,50,24,23,42,49,52,4,30,47,32,50,47,51,48,54,54,47,42,22,33,64,26,64,53,41,68,11,8,49,77,35,41,40,37,81,22,53,84,68,52,82,80,4,14,20,16,35,54],[0,0,1,1,1,2,0,6,6,0,10,2,12,0,5,3,16,0,8,4,10,6,20,3,23,13,11,20,11,26,19,22,16,21,7,24,24,16,23,28,28,5,33,11,4,26,17,15,26,35,40,5,14,47,27,21,51,20,8,39,52,13,0,39,6,19,41,32,36,21,16,59,46,57,62,40,25,64,57,73,47,34,29,22,67,29,50,11,20,31,9,34,76,7,61,19,73,70,50,68],[0,0,1,1,0,0,0,1,2,3,5,5,2,0,12,8,12,13,11,13,12,11,11,18,16,0,14,5,10,0,28,11,20,12,2,11,0,11,11,20,6,13,4,41,3,25,11,46,9,14,30,12,13,12,9,40,7,11,52,45,16,61,0,27,47,58,64,56,27,1,68,65,44,23,29,8,4,44,74,41,11,46,65,44,40,79,17,51,39,30,50,44,31,82,57,35,33,69,26,56],[0,0,1,3,0,5,6,4,2,5,2,9,7,7,7,15,9,8,13,16,2,4,18,5,15,9,8,26,16,8,18,13,0,9,28,0,25,7,27,22,21,10,39,33,19,27,13,41,3,47,42,18,4,18,11,31,7,1,2,39,27,49,3,56,39,4,62,9,0,11,5,26,0,36,21,53,68,23,0,13,60,30,45,77,34,11,45,16,40,13,38,52,45,47,23,65,94,60,60,81],[0,0,2,3,0,5,6,3,3,4,9,6,5,0,11,11,4,11,9,6,11,6,13,3,10,8,15,5,15,26,1,23,26,13,22,29,4,24,6,30,38,28,32,28,30,25,21,40,42,21,3,23,2,52,51,35,27,44,7,12,9,19,9,14,61,41,10,23,25,19,47,43,72,71,16,13,57,59,28,32,55,78,35,32,70,34,76,85,54,29,41,56,8,35,47,94,69,26,6,26],[0,0,2,1,2,5,5,6,3,0,0,6,6,4,3,13,14,4,16,17,6,5,5,20,11,11,10,15,24,19,0,18,18,21,6,3,4,15,20,0,40,27,20,26,21,12,14,13,44,49,8,14,1,25,18,55,50,52,58,7,25,54,62,54,24,51,21,58,51,66,10,45,2,30,20,18,65,62,73,17,14,59,57,23,75,21,15,7,42,23,24,71,6,84,35,50,4,59,67,30],[0,0,1,2,2,4,5,2,3,2,3,5,4,13,6,4,2,1,3,18,11,8,5,4,21,22,8,6,25,0,9,2,17,26,26,31,32,20,8,39,18,0,29,37,34,20,0,18,13,44,4,0,50,29,47,35,30,23,30,35,31,39,36,57,19,19,31,7,38,46,56,49,42,38,65,62,72,66,32,77,46,21,65,69,19,81,52,81,15,25,70,6,4,84,78,47,88,55,94,7],[0,1,0,2,2,0,3,0,8,4,8,8,0,2,3,10,8,8,3,9,1,18,8,16,8,19,13,11,18,11,10,14,25,3,6,34,25,5,20,32,35,18,22,43,32,7,13,14,6,16,27,43,2,1,28,53,25,33,29,12,60,61,41,44,8,38,60,34,21,50,27,54,35,49,40,10,5,4,34,63,7,40,21,64,9,52,27,23,62,43,62,12,49,35,67,43,94,85,61,46],[0,1,0,0,0,5,5,1,0,6,9,7,8,11,5,15,8,17,16,15,7,9,14,10,20,12,25,9,8,0,19,4,11,15,16,10,22,13,21,17,39,19,0,30,20,22,8,5,3,44,2,4,26,2,31,25,40,21,29,47,19,31,50,46,21,32,7,47,21,65,41,8,33,2,27,16,62,25,36,58,7,43,30,28,81,16,60,61,62,6,21,85,3,9,49,20,82,95,86,76],[0,1,2,3,4,2,5,5,0,2,4,5,2,6,9,3,16,1,10,6,15,18,21,22,21,15,16,1,12,20,9,17,31,13,21,20,1,6,17,17,19,30,19,6,31,4,7,45,37,26,50,20,23,44,4,41,50,55,57,22,58,20,29,30,42,15,20,4,26,35,52,51,41,45,21,58,12,57,48,46,7,63,41,77,21,56,45,1,62,76,29,36,33,38,89,24,42,17,93,84],[0,0,1,2,2,1,0,7,4,2,3,10,2,3,12,7,13,5,3,15,14,4,22,4,7,21,7,13,22,24,25,17,12,22,32,26,16,34,1,19,31,23,17,2,35,16,44,4,39,49,45,46,3,19,14,8,43,48,55,29,10,61,12,42,12,19,56,16,37,61,2,33,71,13,38,53,20,77,76,60,59,66,4,67,72,28,7,68,71,68,6,84,1,31,91,40,94,38,49,45],[0,1,0,0,4,4,2,7,8,9,7,7,6,2,11,2,10,10,5,6,19,6,6,19,12,23,22,9,23,5,24,7,4,32,24,3,7,37,22,10,15,21,1,18,14,5,16,38,7,24,46,11,0,0,45,32,44,26,21,28,53,56,53,46,47,0,42,51,33,42,33,44,30,45,31,49,15,69,27,41,12,2,20,52,2,81,19,49,81,2,47,6,74,77,4,94,36,82,1,86],[0,1,0,1,1,0,6,2,8,1,5,11,7,4,8,5,10,0,4,4,19,21,1,20,16,7,2,18,6,11,28,11,3,7,14,26,24,11,14,4,26,16,24,1,37,24,29,24,40,20,20,47,28,24,34,52,27,46,23,21,17,38,54,19,50,47,35,49,43,62,65,30,42,67,72,35,38,75,71,40,65,72,4,28,67,5,52,41,46,50,41,68,58,75,1,40,6,7,90,64],[0,1,0,2,0,0,5,1,2,3,5,1,4,6,8,6,4,6,8,2,14,6,19,4,23,23,4,10,11,8,5,21,26,20,15,29,10,36,6,37,14,27,41,40,3,39,38,23,32,18,38,47,6,8,11,39,53,33,49,44,24,30,30,7,37,10,16,38,27,33,31,20,44,51,22,8,24,50,76,30,35,28,33,1,83,5,63,62,75,46,0,17,46,65,6,3,82,89,33,77],[0,0,2,1,0,2,4,4,1,0,2,3,1,12,0,6,1,14,13,6,1,7,0,16,11,24,13,15,3,23,10,31,26,6,14,27,2,20,35,28,10,10,8,29,44,23,26,38,48,44,30,46,8,4,25,42,45,11,28,34,38,52,30,50,43,38,62,54,64,2,59,8,58,53,26,56,71,67,54,3,42,20,73,34,19,54,84,58,46,72,22,26,23,3,34,92,88,63,89,41],[0,0,2,1,0,1,3,0,7,3,10,0,1,6,7,8,6,2,6,4,19,10,13,15,24,16,21,10,14,16,0,3,15,10,33,18,18,23,2,9,17,26,38,28,12,45,9,12,25,16,28,19,23,39,12,5,36,43,29,19,39,36,5,63,27,20,4,15,46,69,48,36,56,65,17,36,69,69,57,57,29,56,0,74,79,54,38,68,68,8,16,54,50,77,67,29,60,97,86,39],[0,0,2,2,3,2,1,3,1,4,5,0,0,10,11,2,13,1,1,7,8,10,12,23,10,14,7,1,2,0,22,15,5,1,20,13,25,33,7,18,39,37,31,29,19,16,0,27,18,7,8,6,21,7,4,49,16,36,15,24,48,13,48,52,51,57,25,28,5,9,45,62,70,26,8,57,71,3,4,27,13,47,17,70,60,23,55,29,10,29,56,55,2,90,8,21,91,4,16,72],[0,0,0,2,0,5,6,2,3,7,3,5,3,1,7,13,4,13,17,12,12,14,16,7,4,21,23,24,16,7,14,23,12,10,16,1,20,8,12,36,9,36,17,23,37,31,42,31,1,12,44,42,36,45,24,19,14,44,27,46,18,31,44,49,17,56,22,50,49,59,54,68,68,57,63,69,61,14,16,41,40,81,62,26,84,76,74,27,36,72,21,58,19,67,45,16,39,87,69,0],[0,1,1,3,3,4,1,5,2,6,3,10,8,4,12,15,3,10,6,16,5,16,20,18,6,13,15,27,16,23,27,18,29,8,26,33,28,37,32,22,8,4,10,10,26,27,33,41,40,13,31,13,2,11,44,42,22,41,18,31,44,45,42,20,44,41,45,3,50,14,64,39,8,22,42,8,14,73,46,25,49,58,41,52,69,61,44,19,7,40,45,10,17,1,10,12,84,18,27,16]]
print(spiralOrder(matrix))