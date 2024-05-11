import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
q = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    d = abs(x) + abs(y)
    heapq.heappush(q, (d, x, y))

for _ in range(m):
    cd, cx, cy = heapq.heappop(q)
    cx += 2
    cy += 2
    cd = abs(cx) + abs(cy)
    heapq.heappush(q, (cd, cx, cy))

_, cx, cy = heapq.heappop(q)
print(cx, cy)