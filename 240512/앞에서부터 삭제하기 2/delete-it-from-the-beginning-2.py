import sys
import heapq

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
for k in range(1, n-1):
    q = a[k:]
    heapq.heapify(q)
    heapq.heappop(q)
    avg = sum(q) / len(q)
    answer = max(answer, avg)

print("{:.2f}".format(answer))