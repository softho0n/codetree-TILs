import sys
from collections import defaultdict

d = defaultdict(int)
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    d[a[i]] += 1

ans = 0
for i in range(n):
    d[a[i]] -= 1
    target = k - a[i]
    ans += d[target]

print(ans)