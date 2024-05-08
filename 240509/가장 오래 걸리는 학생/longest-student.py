import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
g = [
    []
    for _ in range(n + 1)
]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))
    g[b].append((a, c))

INF = 1000000
distance = [INF] * (n + 1)
distance[n] = 0

q = []
heapq.heappush(q, (0, n))
while q:
    cd, cp = heapq.heappop(q)
    if distance[cp] < cd:
        continue
    
    for np, nd in g[cp]:
        newd = nd + cd
        if newd < distance[np]:
            distance[np] = newd
            heapq.heappush(q, (newd, np))

answer = 0
for i in range(1, n):
    if distance[i] == INF:
        continue
    answer = max(answer, distance[i])

print(answer)