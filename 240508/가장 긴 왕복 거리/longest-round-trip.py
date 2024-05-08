import sys
import heapq



n, m, x = map(int, sys.stdin.readline().split())
graph = [
    []
    for _ in range(n+1)
]

rgraph = [
    []
    for _ in range(n+1)
]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    rgraph[b].append((a, c))

INF = 10000000000
distance1 = [INF] * (n + 1)
distance1[x] = 0
q = []
heapq.heappush(q, (0, x))

while q:
    cd, cp = heapq.heappop(q)

    if distance1[cp] < cd:
        continue
    
    for np, nd in graph[cp]:
        newd = nd + cd
        if newd < distance1[np]:
            distance1[np] = newd
            heapq.heappush(q, (newd, np))

INF = 10000000000
distance2 = [INF] * (n + 1)
distance2[x] = 0
q = []
heapq.heappush(q, (0, x))

while q:
    cd, cp = heapq.heappop(q)

    if distance2[cp] < cd:
        continue
    
    for np, nd in rgraph[cp]:
        newd = nd + cd
        if newd < distance2[np]:
            distance2[np] = newd
            heapq.heappush(q, (newd, np))

answer = 0
for i in range(1, n + 1):
    if i == x:
        continue
    tmp = distance1[i] + distance2[i]
    if tmp >= INF:
        continue
    answer = max(answer, tmp)
print(answer)