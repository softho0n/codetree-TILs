import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = -1
# ---
for i in range(n):
    for j in range(m-2):
        answer = max(answer, graph[i][j] + graph[i][j+1] + graph[i][j+2])

# |
# |
# |
for j in range(m):
    for i in range(n-2):
        answer = max(answer, graph[i][j] + graph[i+1][j] + graph[i+2][j])

# |
# | |
for i in range(n):
    for j in range(m):
        if i + 1 < n and j + 1 < m:
            answer = max(answer, graph[i][j] + graph[i+1][j] + graph[i+1][j+1])

#   |
# | |
for i in range(n):
    for j in range(m):
        if i + 1 < n and j < m:
            answer = max(answer, graph[i][j] + graph[i+1][j] + graph[i+1][j-1])

# | |
# |
for i in range(n):
    for j in range(m):
        if i + 1 < n and j + 1 < m:
            answer = max(answer, graph[i][j] + graph[i][j+1] + graph[i+1][j])

# | |
#   |
for i in range(n):
    for j in range(m):
        if i + 1 < n and j + 1 < m:
            answer = max(answer, graph[i][j] + graph[i][j+1] + graph[i+1][j+1])

print(answer)