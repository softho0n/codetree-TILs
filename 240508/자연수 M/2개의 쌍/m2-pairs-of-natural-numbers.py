import sys
import heapq

n = int(sys.stdin.readline().rstrip())
s = []
m = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a >= 2:
        a = 2
    m += a
    for _ in range(a):
        s.append(b)

s.sort()
ans = 1000000001
# print(s)
for i in range(0, m // 2):
    tmp_sum = s[i] + s[m-i-1]
    ans = min(ans, tmp_sum)

print(ans)