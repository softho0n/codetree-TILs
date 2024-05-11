import sys

n, m = map(int, sys.stdin.readline().split())

from collections import defaultdict

d = defaultdict(int)
idx = 1
for _ in range(n):
    s = input()
    d[s] = idx
    idx += 1

for _ in range(m):
    s = input()
    if s.isalpha():
        print(d[s])
    else:
        for k, v in d.items():
            if v == int(s):
                print(k)