import sys





from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(
        list(map(int, sys.stdin.readline().split()))
    )

v = [
    [False] * (m+1)
    for _ in range(n+1)
]

q = deque()
q.append((0, 0))
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

v[0][0] = True

while q:
    cy, cx = q.popleft()

    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        
        if v[ny][nx]:
            continue
        
        if graph[ny][nx] == 1:
            v[ny][nx] = True
            q.append((ny, nx))
            graph[ny][nx] = graph[cy][cx] + 1

if v[n-1][m-1] is False:
    print(-1)
else:
    print(graph[n-1][m-1]-1)