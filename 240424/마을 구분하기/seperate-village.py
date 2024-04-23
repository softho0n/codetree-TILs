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

def dfs(y, x, cnt):
    global tmp_answer
    tmp_answer = max(tmp_answer, cnt)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue

        if visited[ny][nx]:
            continue

        if graph[ny][nx] == 1:
            visited[ny][nx] = True
            dfs(ny, nx, cnt + 1)

cnt = 0
sample = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] is False:
            tmp_answer = 0
            visited[i][j] = True
            dfs(i, j, 1)
            sample.append(tmp_answer)
            cnt += 1

sample.sort()
print(cnt)
for item in sample:
    print(item)