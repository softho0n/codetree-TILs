import sys
import heapq

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
q = []
heapq.heappush(q, a[-1])
for k in range(n-2, 0, -1):
    heapq.heappush(q, a[k])
    v = heapq.heappop(q)

    avg = sum(q) / (n - (k + 1))
    answer = max(answer, avg)
    heapq.heappush(q, v)


print("{:.2f}".format(answer))