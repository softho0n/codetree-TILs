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

b = Counter(d).most_common(k)
b.sort(key=lambda x: (x[1], x[0]))
b = b[::-1]
for item in b:
    print(item[0], end=' ')