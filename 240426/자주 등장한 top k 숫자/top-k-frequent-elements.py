import sys
from collections import Counter

n, k = map(int, sys.stdin.readline().split())
d = {}

a = list(map(int, sys.stdin.readline().split()))
for item in a:
    if not item in d:
        d[item] = 1
    else:
        d[item] += 1

s = []
for k, v in d.items():
    s.append((k, v))

s.sort(key=lambda x:(x[1], x[0]))
s = s[::-1]
s = s[:k]
for item in s:
    print(item[0], end=' ')