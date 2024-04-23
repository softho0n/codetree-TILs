import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dy = [0, 0, 1, -1]
dx = [1, 1, 0, 0]

visited = [
    [False for _ in range(m+1)]
    for _ in range(n+1)
]

def dfs(sy, sx):
    for k in range(4):
        ny, nx = sy + dy[k], sx + dx[k]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if visited[ny][nx] is False and graph[ny][nx] == 1:
            visited[ny][nx] = True
            dfs(ny, nx)
            visited[ny][nx] = False


visited[0][0] = True
dfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)