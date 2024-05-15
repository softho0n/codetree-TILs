import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
ps = [0] * (n + 1)

ps[0] = a[0]
for i in range(1, n):
    ps[i] = ps[i-1] + a[i]

answer = 0
for i in range(n):
    if i + k >= n:
        continue
    answer = max(answer, ps[i+k] - ps[i])
print(answer)