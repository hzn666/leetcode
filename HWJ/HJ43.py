def dfs(maze, i, j, route):
    if i == n - 1 and j == m - 1:
        for pos in route:
            print('(' + str(pos[0]) + ',' + str(pos[1]) + ')')
        return

    if 0 <= i - 1 < n and 0 <= j < m and maze[i - 1][j] == 0:
        maze[i - 1][j] = 1
        dfs(maze, i - 1, j, route + [(i - 1, j)])
        maze[i - 1][j] = 0
    if 0 <= i + 1 < n and 0 <= j < m and maze[i + 1][j] == 0:
        maze[i + 1][j] = 1
        dfs(maze, i + 1, j, route + [(i + 1, j)])
        maze[i + 1][j] = 0
    if 0 <= i < n and 0 <= j - 1 < m and maze[i][j - 1] == 0:
        maze[i][j - 1] = 1
        dfs(maze, i, j - 1, route + [(i, j - 1)])
        maze[i][j - 1] = 0
    if 0 <= i < n and 0 <= j + 1 < m and maze[i][j + 1] == 0:
        maze[i][j + 1] = 1
        dfs(maze, i, j + 1, route + [(i, j + 1)])
        maze[i][j + 1] = 0
    return


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    maze[0][0] = 1
    dfs(maze, 0, 0, [(0, 0)])
