row, col = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(row)]


def bfs(maze, row, col):
    queue = []
    path = [[0]*col for _ in range(row)]
    visited = [[False]*col for _ in range(row)]

    queue.append((0, 0))
    path[0][0] = 1
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                path[nx][ny] = path[x][y] + 1
                queue.append((nx, ny))
    return path[row-1][col-1]


newpath = bfs(maze, row, col)


print(newpath)


