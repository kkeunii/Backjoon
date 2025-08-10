col, row = map(int, input().split())
paintings = [list(map(int, input().split())) for _ in range(col)]
count = 0
wide = 0
visited = [[False]*row for _ in range(col)]

def bfs(paintings, start, visited):
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = True
    wide = 0
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        x, y = queue.pop(0)
        wide += 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < col and 0 <= ny < row and not visited[nx][ny] and paintings[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return wide

for p in range(col):
    for q in range(row):
        if paintings[p][q] == 1 and not visited[p][q]:
            count += 1
            newwide = bfs(paintings, (p, q), visited)
            if wide < newwide:
                wide = newwide

print(count, wide)
