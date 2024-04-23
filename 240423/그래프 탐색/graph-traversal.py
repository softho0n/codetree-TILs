import sys
n, m = map(int, sys.stdin.readline().split())
graph = [
    [] for _ in range(n+1)
]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n+1)]

answer = 0
def dfs(start):
    for next_pos in graph[start]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            dfs(next_pos)

visited[1] = True
dfs(1)

for i in range(2, n+1):
    if visited[i]:
        answer += 1
print(answer)