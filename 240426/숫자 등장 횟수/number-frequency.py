import sys
n, m = map(int, sys.stdin.readline().split())
d = {}
a = list(map(int, sys.stdin.readline().split()))

for item in a:
    if not item in d:
        d[item] = 1
    else:
        d[item] += 1
m_l = list(map(int, sys.stdin.readline().split()))
for item in m_l:
    if not item in d:
        print(0, end=' ')
    else:
        print(d[item], end=' ')