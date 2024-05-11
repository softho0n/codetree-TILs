import heapq
import sys

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(q, -x)
    elif x == 0:
        if q:
            v = heapq.heappop(q)
            print(-v)
        else:
            print(0)