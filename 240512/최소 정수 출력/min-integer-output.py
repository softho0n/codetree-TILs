import heapq
import sys
n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(q) != 0:
            v = heapq.heappop(q)
            print(v)
        else:
            print(0)
    else:
        heapq.heappush(q, x)