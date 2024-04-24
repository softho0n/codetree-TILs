import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

r, c = map(int, sys.stdin.readline().split())
r = r - 1
c = c - 1


visited = [
    [False] * n
    for _ in range(n)
]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x, sample):
    q = deque()
    visited[y][x] = True
    q.append((y, x))

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            
            if visited[ny][nx]:
                continue

            if graph[ny][nx] < sample:
                q.append((ny, nx))
                visited[ny][nx] = True
    
    candidate = []
    for i in range(n):
        for j in range(n):
            if i == y and j == x:
                continue

            if visited[i][j]:
                candidate.append((i, j, graph[i][j]))
    
    if len(candidate) == 0:
        return y, x

    candidate.sort(lambda x:(-x[2]))
    return candidate[0][0], candidate[0][1]
    
for _ in range(k):
    
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    
    r, c = bfs(r, c, graph[r][c])


print(r+1, c+1)