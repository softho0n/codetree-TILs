import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
answer = 0
visited = [
    [False] * n
    for _ in range(n)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

starts = []
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    r = r - 1
    c = c - 1
    starts.append((r, c))

def bfs(y, x):
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
            
            if graph[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((ny, nx))

def go(cnt):
    if cnt == m:
        for i in range(n):
            for j in range(n):
                visited[i][j] = False

        for sy, sx in starts:
            bfs(sy, sx)
        
        tmp_cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    tmp_cnt += 1
        global answer

        answer = max(answer, tmp_cnt)        
        return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    go(cnt + 1)
                    graph[i][j] = 1

go(0)
print(answer)