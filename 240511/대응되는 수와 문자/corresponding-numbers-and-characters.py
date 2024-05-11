import sys

n, m = map(int, sys.stdin.readline().split())

from collections import defaultdict

d = defaultdict(int)
d1 = defaultdict(str)
idx = 1
for _ in range(n):
    s = input()
    d[s] = idx
    d1[idx] = s
    idx += 1

for _ in range(m):
    s = input()
    if s.isalpha():
        print(d[s])
    else:
        print(d1[int(s)])