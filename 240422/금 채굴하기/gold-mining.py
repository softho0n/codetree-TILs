import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0

def calc(i, j, k):
    sample = []

    step = 0
    for y in range(i, i+k+1):
        for x in range(j-k+step, j+k-step+1):
            sample.append((y, x))
        step += 1
    
    step = 1
    for y in range(i-1, i-k-1, -1):
        for x in range(j-k+step, j+k-step+1):
            sample.append((y, x))
        step += 1

    tmp_cnt = 0
    for y, x in sample:
        if y < 0 or x < 0 or y >= n or x >= n:
            continue
        
        if graph[y][x] == 1:
            tmp_cnt += 1
    
    total_value = k * k + (k + 1) * (k + 1)
    credit = tmp_cnt * m
    if credit >= total_value:
        global answer
        answer = max(answer, tmp_cnt)

for k in range(n):
    for i in range(n):
        for j in range(n):
            calc(i, j, k)

print(answer)