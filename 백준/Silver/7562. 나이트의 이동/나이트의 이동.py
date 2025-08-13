def bfs(box, row,  start, end):
    queue = []
    col = row
    visited = [[False]*col for _ in range(row)]

    queue.append((start[0], start[1]))
    box[start[0]][start[1]] = 0
    first_dir = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    if start == end:
        return 0
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in first_dir:
            nx, ny = x + dx , y + dy 
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                visited[nx][ny] = True
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
            if nx == end[0] and ny == end[1]:
                return box[end[0]][end[1]]
                
    return box[end[0]][end[1]]

num = int(input())
for _ in range(num):
    row = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    box = [[0]*row for _ in range(row)]

    print(bfs(box, row, start, end))
