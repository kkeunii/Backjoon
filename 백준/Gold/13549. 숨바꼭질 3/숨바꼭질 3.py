subin, sister = map(int, input().split())
maxnum = 100001

def bfs(subin, sister, maxnum):
    queue = []
    time = [-1 for _ in range(maxnum)]
    
    time[subin] = 0
    queue.append(subin)

    if subin == sister:
        return 0

    while queue and time[sister] == -1:
        x = queue.pop(0)
        direction = [2, -1, +1]

        for p in direction:
            if p == 2:
                nx = x * 2
            else:
                nx = x + p

            if 0 <= nx < maxnum and time[nx] == -1 and p == 2:
                time[nx] = time[x]
                queue.insert(0, nx)
            elif 0 <= nx < maxnum and time[nx] == -1:
                time[nx] = time[x] + 1
                queue.append(nx)

    return time[sister]


fastest = bfs(subin, sister, maxnum)
print(fastest)
