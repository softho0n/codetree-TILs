import sys


n = int(input())

graph = [
    [0] * n
    for _ in range(n)
]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
curd = 0
step = 1
graph[n // 2][n // 2] = 1
y = n // 2
x = n // 2
ny, nx = y, x

def end(y, x):
    if y < 0 or x < 0 or y >= n or x >= n:
        return True
    return False

item = 1
while not end(ny, nx):
    for _ in range(step):
        graph[ny][nx] = item
        item += 1

        ny = ny + dy[curd]
        nx = nx + dx[curd]

        if end(ny, nx):
            break
    
    curd = (curd + 1) % 4
    if curd == 0 or curd == 2:
        step += 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()