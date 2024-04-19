import sys
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = -1
for i in range(n):
    for j in range(n-2):
        answer = max(answer, graph[i][j] + graph[i][j+1] + graph[i][j+2])

print(answer)