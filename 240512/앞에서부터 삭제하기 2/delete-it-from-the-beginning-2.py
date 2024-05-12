import sys
import heapq

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
q = []
heapq.heappush(q, a[-1])
tmp_sum = a[-1]
for k in range(n-2, 0, -1):
    heapq.heappush(q, a[k])
    tmp_sum += a[k]
    v = q[0]
    
    avg = (tmp_sum - v) / (n - (k + 1))
    answer = max(answer, avg)


print("{:.2f}".format(answer))