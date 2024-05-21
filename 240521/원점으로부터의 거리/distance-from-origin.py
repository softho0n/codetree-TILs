import sys
n = int(input())

p = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    p.append((abs(x) + abs(y), i, x, y))

p.sort()
for d, n, _, _ in p:
    print(n+1)