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
b.sort()
b = b[::-1]
for item in b:
    print(item[0], end=' ')
# c = []
# for item in b:
#     c.append(item[0])
# c.sort(reverse=True)
# for item in c:
#     print(item, end=' ')