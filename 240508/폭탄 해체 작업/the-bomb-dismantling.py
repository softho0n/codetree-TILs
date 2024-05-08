import sys
import heapq
n = int(input())
info = []

for _ in range(n):
    v, w = map(int, sys.stdin.readline().split())
    info.append((w, v))

info.sort()
idx = n - 1

pq = []
answer = 0
for i in range(10001, 0, -1):
    while idx >= 0 and info[idx][0] >= i:
        heapq.heappush(pq, -info[idx][1])
        idx -= 1
    
    if pq:
        answer += -heapq.heappop(pq)

print(answer)