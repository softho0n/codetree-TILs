import heapq
import sys

n, m, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()

q = []
for i in range(n):
    heapq.heappush(q, (a[i] + b[0], a[i], b[0], 0))

answer = 0
for _ in range(k):
    s, x, y, idx = heapq.heappop(q)
    answer = s
    if idx == m-1:
        continue
    heapq.heappush(q, (x + b[idx + 1], x, b[idx + 1], idx + 1))

print(answer)