import heapq
import sys

n = int(input())
q = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if q:
            v, z = heapq.heappop(q)
            print(z)
        else:
            print(0)