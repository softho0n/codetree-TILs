import sys



from collections import deque
import heapq


n = int(input())
q = []
heapq.heappush(q, (0, n))
answer = 0
while q:
    cv, cp = heapq.heappop(q)

    if cp == 1:
        answer = cv
        break

    heapq.heappush(q, (cv + 1, cp + 1))
    heapq.heappush(q, (cv + 1, cp - 1))

    if cp % 2 == 0:
        heapq.heappush(q, (cv + 1, cp // 2))
    
    if cp % 3 == 0:
        heapq.heappush(q, (cv + 1, cp // 3))
print(answer)