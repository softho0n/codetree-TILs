import sys
from collections import deque
n, k, u, d = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
v = [
    [False] * n
    for _ in range(n)
]
s = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = 0
def bfs():
    for i in range(n):
        for j in range(n):
            v[i][j] = False

    q = deque()
    for y, x in s:
        q.append((y, x))
        v[y][x] = True
    
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            
            if v[ny][nx]:
                continue
            
            val = abs(graph[ny][nx] - graph[cy][cx])
            if val >= u and val <= d:
                v[ny][nx] = True
                q.append((ny, nx))
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if v[i][j]:
                cnt += 1
    
    return cnt


def go(cnt):
    if cnt == k:
        cnt = bfs()
        global answer
        answer = max(answer, cnt)
        return
    else:
        for i in range(n):
            for j in range(n):
                if not (i, j) in s:
                    s.append((i, j))
                    go(cnt + 1)
                    s.pop()

go(0)
print(answer)