import sys


n, m = map(int, sys.stdin.readline().split())

graph = [
    [0] * (m)
    for _ in range(n)
]

graph[0][0] = 1

# 아래쪽 -> 오른쪽 -> 위쪽 -> 왼쪽 -> 아래쪽 -> 오른쪽 -> 위쪽 -> 왼쪽 ... 반복
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cur_d = 0
y, x = 0, 0
for item in range(2, n * m + 1):
    ny, nx = y + dy[cur_d], x + dx[cur_d]
    if (ny < 0 or nx < 0 or ny >= n or nx >= m) or graph[ny][nx] != 0:
        cur_d = (cur_d + 1) % 4

    ny, nx = y + dy[cur_d], x + dx[cur_d]
    graph[ny][nx] = item
    y, x = ny, nx

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()