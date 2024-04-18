import sys



n, m = map(int, sys.stdin.readline().split())
graph = [
    [''] * (m)
    for _ in range(n)
]

graph[0][0] = 'A'
from string import ascii_uppercase

# 26개 A to Z
alphabet = list(ascii_uppercase)
cur_d = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
y, x = 0, 0

for i in range(1, n * m):
    ny = y + dy[cur_d]
    nx = x + dx[cur_d]

    if (ny < 0 or nx < 0 or ny >= n or nx >=m) or graph[ny][nx] != '':
        cur_d = (cur_d + 1) % 4
    
    ny = y + dy[cur_d]
    nx = x + dx[cur_d]
    y = ny
    x = nx

    graph[ny][nx] = alphabet[i % 26]

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()