import sys
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if j == l and i == k:
                    continue
                tmp_sum = graph[i][j] + graph[i][j+1] + graph[i][j+2]
                tmp_sum += (graph[k][l] + graph[k][l+1] + graph[k][l+2])

                answer = max(answer, tmp_sum)

print(answer)