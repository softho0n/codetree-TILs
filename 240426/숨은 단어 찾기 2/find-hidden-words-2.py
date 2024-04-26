import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, -1, -1, 1]

def can_go(y, x):
    if y >= 0 and x >= 0 and y < n and x < m:
        return True
    return False

answer = 0

def solve(y, x):
    for k in range(8):
        tmp = ['L']
        for step in range(1, 3):
            ny, nx = y + dy[k] * step, x + dx[k] * step
            if can_go(ny, nx):
                tmp.append(graph[ny][nx])
            else:
                break
            
        if len(tmp) == 3:
            if tmp[1] == 'E' and tmp[2] == 'E':
                global answer
                answer += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            solve(i, j)

print(answer)