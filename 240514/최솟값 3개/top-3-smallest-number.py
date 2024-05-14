import heapq
import sys

q = []
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    heapq.heappush(q, a[i])

    if len(q) < 3:
        print(-1)
    else:
        z = heapq.heappop(q)
        x = heapq.heappop(q)
        o = heapq.heappop(q)
        print(z * x * o)
        heapq.heappush(q, z)
        heapq.heappush(q, x)
        heapq.heappush(q, o)