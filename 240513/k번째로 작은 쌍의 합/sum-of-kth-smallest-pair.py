import heapq
import sys

n, m, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()

q = []
for i in range(n):
    heapq.heappush(q, (a[i] + b[0], a[i], b[0], i))

while True:
    k -= 1
    s, x, y, idx = heapq.heappop(q)
    if k == 0:
        print(s)
        break

    heapq.heappush(q, (x + b[idx + 1], x, b[idx + 1], idx + 1))