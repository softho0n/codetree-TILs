import sys
n, k = map(int, sys.stdin.readline().split())
from collections import defaultdict
a = list(map(int, sys.stdin.readline().split()))

d = defaultdict(int)
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