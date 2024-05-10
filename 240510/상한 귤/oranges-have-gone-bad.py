import sys



from collections import deque
n, k = map(int, sys.stdin.readline().split())
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

v = [
    [False] * (n + 1)
    for _ in range(n + 1)
]

c = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

q = deque()
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            q.append((i, j))
            v[i][j] = True

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

while q:
    cy, cx = q.popleft()

    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        
        if v[ny][nx]:
            continue
        
        if g[ny][nx] == 1:
            v[ny][nx] = True
            c[ny][nx] = c[cy][cx] + 1
            q.append((ny, nx))

for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            print(-1, end=' ')
        else:
            if v[i][j] is True:
                print(c[i][j], end=' ')
            else:
                print(-2, end=' ')
    print()