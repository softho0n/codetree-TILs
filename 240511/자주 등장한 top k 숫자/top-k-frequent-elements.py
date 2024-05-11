import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

d = defaultdict(int)
for item in a:
    d[item] += 1

K = []
for b, v in d.items():
    K.append((b, v))

K.sort(key=lambda x: (-x[1], -x[0]))
for i in range(k):
    print(K[i][0], end=' ')