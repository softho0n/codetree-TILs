import sys
from collections import deque
n = int(input())
g = []

for _ in range(n):
    row = list(sys.stdin.readline().rstrip())
    g.append(row)

coins = []
sx, sy, ex, ey = -1, -1, -1, -1
for i in range(n):
    for j in range(n):
        if g[i][j] != '.' and g[i][j] != 'S' and g[i][j] != 'E':
            coin_num = int(g[i][j])
            coins.append((coin_num, (i, j)))
        if g[i][j] == 'S':
            sx, sy = i, j
        if g[i][j] == 'E':
            ex, ey = i, j

subset = []
answer = 1000000000

def get_distance(c):
    tmp_distance = vertex_distance((sx, sy), c[0][1])
    for i in range(0, len(c)-1):
        tmp_distance += vertex_distance(c[i][1], c[i+1][1])

    tmp_distance += vertex_distance(c[-1][1], (ex, ey))
    # print(c, tmp_distance)
    return tmp_distance

def vertex_distance(s, e):
    distance = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    visited = [
        [False] * (n + 1)
        for _ in range(n + 1)
    ]

    q = deque()
    q.append(s)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        cx, cy = q.popleft()

        if cx == e[0] and cy == e[1]:
            break

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            distance[nx][ny] = distance[cx][cy] + 1
            q.append((nx, ny))

    # print(f"start ({s}) end ({e}) distance ({distance[e[0]][e[1]]})")
    return distance[e[0]][e[1]]


def solution():
    c = subset[::]
    c.sort()

    distance = get_distance(c)
    global answer
    answer = min(answer, distance)

def go(cnt, idx):
    if cnt == 3:
        solution()
        return
    else:
        for i in range(idx, len(coins)):
            subset.append(coins[i])
            go(cnt + 1, i + 1)
            subset.pop()
if len(coins) < 3:
    print(-1)
    exit(0)
go(0, 0)
print(answer)