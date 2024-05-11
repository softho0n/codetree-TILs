import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
q = []
for item in a:
    heapq.heappush(q, -item)

for _ in range(m):
    v = heapq.heappop(q)
    v = -v
    v = v - 1
    heapq.heappush(q, -v)

v = heapq.heappop(q)
print(-v)