import sys
from collections import defaultdict

d = defaultdict(int)
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    d[a[i]] += 1

ans = 0
min_v = min(a)
max_v = max(a)
for i in range(min_v, max_v + 1):
    tmp = d[i]
    tmp2 = d[k-i]

    ans += tmp * tmp2

print(ans // 2)