import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
g = [
    []
    for _ in range(n+1)
]

for _ in range(m):
    s, t, d = map(int, sys.stdin.readline().split())
    g[t].append((s, d))

INF = 10000000000
distance = [INF] * (n + 1)
distance[n] = 0

q = []
heapq.heappush(q, (0, n))

while q:
    curd, curp = heapq.heappop(q)

    if distance[curp] < curd:
        continue
    
    for nextp, nextd in g[curp]:
        newd = curd + nextd

        if newd < distance[nextp]:
            distance[nextp] = newd
            heapq.heappush(q, (newd, nextp))

answer = 0
for i in range(1, n):
    if distance[i] == INF:
        continue
    answer = max(answer, distance[i])
print(answer)