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
def dfs(start, cnt):
    global answer
    answer = max(answer, cnt)
    
    for next_pos in graph[start]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            dfs(next_pos, cnt + 1)

visited[1] = True
dfs(1, 0)
print(answer)