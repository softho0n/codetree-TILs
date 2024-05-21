import sys
n = int(input())
p = []
for _ in range(n):
    n, h, w = sys.stdin.readline().split()
    p.append((n, int(h), int(w)))
p.sort(key=lambda x: (x[1], -x[2]))
for n, h, w in p:
    print(n, h, w)