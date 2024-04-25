import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 1000000001
for i in range(n):
    sample = a[i]
    tmp_sum = 0
    for j in range(n):
        tmp_sum += a[j] * abs(i - j)
    
    answer = min(answer, tmp_sum)
print(answer)