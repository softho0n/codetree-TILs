import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
answer = 0


tmp_sum = 0
for i in range(n):
    tmp_sum += a[i]
    answer = max(answer, tmp_sum)
    if tmp_sum < 0:
        tmp_sum = 0

print(answer)