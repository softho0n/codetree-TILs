import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [
    [False] * (m + 1)
    for _ in range(n + 1)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    visited[y][x] = True
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            
            if visited[ny][nx]:
                continue
            
            if graph[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx))

bfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)