import heapq
import sys

t = int(input())

def insert(item, min_h, max_h):
    if len(min_h) == len(max_h):
        heapq.heappush(max_h, -item)
    else:
        heapq.heappush(min_h, item)
    
    if min_h and -max_h[0] > min_h[0]:
        max_top = -heapq.heappop(max_h)
        min_top = heapq.heappop(min_h)

        heapq.heappush(min_h, max_top)
        heapq.heappush(max_h, -min_top)

for _ in range(t):
    n = int(input())
    
    a = list(map(int, sys.stdin.readline().split()))
    max_h = []
    min_h = []

    for i in range(n):
        insert(a[i], min_h, max_h)
        if i % 2 == 0:
            print(-max_h[0], end=' ')
    print()