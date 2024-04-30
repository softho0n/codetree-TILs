import sys

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n-2):
    for j in range(n-2):
        tmp_sum = 0
        for k in range(3):
            for p in range(3):
                tmp_sum += g[i+k][j+p]
        
        answer = max(answer, tmp_sum)

print(answer)