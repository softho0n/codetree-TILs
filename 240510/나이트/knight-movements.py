import sys
from collections import deque


n = int(input())

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

graph = [
    [0] * (n+1)
    for _ in range(n+1)
]

v = [
    [False] * (n+1)
    for _ in range(n+1)
]

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

v[r1][c1] = True
q = deque()
q.append((r1, c1))

while q:
    cy, cx = q.popleft()

    for k in range(8):
        ny, nx = cy + dy[k], cx + dx[k]

        if ny < 1 or nx < 1 or ny > n or nx > n:
            continue
        
        if v[ny][nx]:
            continue
        
        v[ny][nx] = True
        graph[ny][nx] = graph[cy][cx] + 1
        q.append((ny, nx))

if v[r2][c2] is False:
    print(-1)
else:
    print(graph[r2][c2])