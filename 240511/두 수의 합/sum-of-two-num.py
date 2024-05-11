import sys
from collections import defaultdict

d = defaultdict(int)
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    d[a[i]] += 1

ans = 0

for K, v in d.items():
    if k-K in d:
        tmp = v * d[k-K]
        ans += tmp

print(ans // 2)