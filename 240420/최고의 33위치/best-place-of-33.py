import sys

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = -1

def get_temp_local(i, j):
    tmp_sum = 0
    for x in range(3):
        for y in range(3):
            tmp_sum += graph[i+x][j+y]
    return tmp_sum


for i in range(n-2):
    for j in range(n-2):
        answer = max(answer, get_temp_local(i, j))

print(answer)