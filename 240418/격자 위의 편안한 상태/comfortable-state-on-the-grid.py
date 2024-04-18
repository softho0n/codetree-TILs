import sys





n, m = map(int, sys.stdin.readline().split())
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    y = y - 1
    x = x - 1
    graph[y][x] = 1
    state = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny >= 0 and nx >= 0 and ny < n and nx < n:
            if graph[ny][nx] > 0:
                state += 1
    
    if state == 3:
        print(1)
    else:
        print(0)