import sys

n, m = map(int, sys.stdin.readline().split())
d = {}
d1 = {}
for i in range(n):
    s = input()
    d[s] = i + 1
    d1[i + 1] = s

for _ in range(m):
    s = input()
    if s.isalpha():
        print(d[s])
    else:
        print(d1[int(s)])