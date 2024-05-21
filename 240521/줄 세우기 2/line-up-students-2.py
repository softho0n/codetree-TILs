import sys
n = int(input())
p = []
for i in range(n):
    h, w = map(int, sys.stdin.readline().split())
    p.append((h, w, i+1))

p.sort(key=lambda x: (x[0], -x[1]))
for h, w, n in p:
    print(h, w, n)