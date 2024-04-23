import sys

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [
    [False] * (n+1)
    for _ in range(n+1)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
tmp_answer = 0

def dfs(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue

        if visited[ny][nx]:
            continue

        if graph[ny][nx] == 1:
            global tmp_answer
            visited[ny][nx] = True
            tmp_answer += 1
            dfs(ny, nx)
    
    return tmp_answer

cnt = 0
sample = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] is False:
            tmp_answer = 1
            visited[i][j] = True
            sample.append(dfs(i, j))
            cnt += 1

sample.sort()
print(cnt)
for item in sample:
    print(item)