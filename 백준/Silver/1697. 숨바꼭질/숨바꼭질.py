subin, sister = map(int, input().split())
maxnum = 100001

def bfs(subin, sister, maxnum):
    queue = []
    path = [-1 for _ in range(maxnum)]
    
    path[subin] = 0
    queue.append(subin)

    if subin == sister:
        return 0

    while queue and path[sister] == -1:
        x = queue.pop(0)
        direction = [x+1, x-1, x*2]

        for nx in direction:
            if 0 <= nx < maxnum and path[nx] == -1:
                path[nx]= path[x] + 1
                queue.append(nx)

    return path[sister]


fastest = bfs(subin, sister, maxnum)
print(fastest)
