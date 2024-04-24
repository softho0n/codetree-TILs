import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [
    [False] * (n)
    for _ in range(n)
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
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            
            if visited[ny][nx]:
                continue
            
            if graph[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((ny, nx))

for _ in range(k):
    yy, xx = map(int, sys.stdin.readline().split())
    yy = yy - 1
    xx = xx - 1
    bfs(yy, xx)

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1

print(cnt)