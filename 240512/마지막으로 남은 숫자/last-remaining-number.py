import heapq
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
q = []

for item in a:
    heapq.heappush(q, -item)

while True:
    if len(q) == 0:
        print(-1)
        break
    elif len(q) == 1:
        print(-q[0])
        break
    
    v1 = -heapq.heappop(q)
    v2 = -heapq.heappop(q)
    v3 = abs(v1 - v2)

    if v3 == 0:
        continue
    
    heapq.heappush(q, -v3)