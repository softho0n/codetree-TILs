import sys

n, k = map(int, sys.stdin.readline().split())
c = []
for _ in range(n):
    c.append(int(input()))

answer = 0
idx = n - 1
while k != 0:
    tmp = k // c[idx]
    k = k - tmp * c[idx]
    idx = idx - 1
    answer += tmp

print(answer)