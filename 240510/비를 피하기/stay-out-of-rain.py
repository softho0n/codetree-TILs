import sys
from collections import deque

n, h, m = map(int, sys.stdin.readline().split())

human_pos = []
m_pos = []
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if g[i][j] == 3:
            m_pos.append((i, j))
        elif g[i][j] == 2:
            human_pos.append((i, j))


answer = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for hp in human_pos:
    hpy, hpx = hp

    q = deque()
    v = [
        [False] * (n + 1)
        for _ in range(n + 1)
    ]
    v[hpy][hpx] = True
    cost = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]
    q.append((hpy, hpx))
    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if v[ny][nx]:
                continue
            if g[ny][nx] != 1:
                v[ny][nx] = True
                cost[ny][nx] = cost[cy][cx] + 1
                q.append((ny, nx))
    
    min_time = 10000000000
    flag = False
    for mp in m_pos:
        mpy, mpx = mp
        if v[mpy][mpx] is False:
            continue
        min_time = min(min_time, cost[mpy][mpx])
        flag = True

    if flag:
        answer[hpy][hpx] = min_time
    else:
        answer[hpy][hpx] = -1

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()