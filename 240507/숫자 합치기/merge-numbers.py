import sys
import heapq

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

q = []
for item in a:
    heapq.heappush(q, item)

answer = 0
while True:
    if len(q) == 1:
        break
    
    a1, a2 = heapq.heappop(q), heapq.heappop(q)
    a3 = a1 + a2
    answer += a3
    heapq.heappush(q, a3)

print(answer)