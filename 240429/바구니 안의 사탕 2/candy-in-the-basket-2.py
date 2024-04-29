import sys

n, k = map(int, sys.stdin.readline().split())
candy = [0] * 10001

for _ in range(n):
    m, x = map(int, sys.stdin.readline().split())
    candy[x] += m

answer = 0
for i in range(k, 10000-k+1):
    tmp_sum = 0
    for j in range(i-k, i+k+1):
        tmp_sum += candy[j]
    
    answer = max(answer, tmp_sum)

print(answer)