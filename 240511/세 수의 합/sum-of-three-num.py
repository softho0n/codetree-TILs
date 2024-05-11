import sys
from collections import defaultdict

d = defaultdict(int)
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
for item in a:
    d[item] += 1

ans = 0

for i in range(n):
    d[a[i]] -= 1
    for j in range(i):
        tmp = k - (a[i] + a[j])
        if tmp in d:
            ans += d[tmp]
print(ans)