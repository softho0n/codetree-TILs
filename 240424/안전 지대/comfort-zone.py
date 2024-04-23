import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [
    [False] * (m + 1)
    for _ in range(n + 1)
]
min_v = 101
max_v = -1

for i in range(n):
    for j in range(m):
        if graph[i][j] < min_v:
            min_v = graph[i][j]
        
        if graph[i][j] > max_v:
            max_v = graph[i][j]


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x, k):
    for p in range(4):
        ny = y + dy[p]
        nx = x + dx[p]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        
        if visited[ny][nx]:
            continue

        if graph[ny][nx] > k:
            visited[ny][nx] = True
            dfs(ny, nx, k)

candidate = []
for k in range(min_v, max_v):
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > k and visited[i][j] is False:
                dfs(i, j, k)
                cnt += 1
    
    candidate.append((cnt, k))

candidate.sort(lambda x: (-x[0]))
print(candidate[0][1], candidate[0][0])