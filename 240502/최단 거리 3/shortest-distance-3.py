import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
g = [
    []
    for _ in range(n+1)
]

for _ in range(m):
    s, t, d = map(int, sys.stdin.readline().split())
    g[s].append((t, d))
    g[t].append((s, d))

a, b = map(int, sys.stdin.readline().split())
INF = 10000000000
distance = [INF] * (n + 1)
distance[a] = 0

q = []
heapq.heappush(q, (0, a))
while q:
    curd, curp = heapq.heappop(q)

    if distance[curp] < curd:
        continue
    
    for nextp, nextd in g[curp]:
        newd = nextd + curd

        if newd < distance[nextp]:
            distance[nextp] = newd
            heapq.heappush(q, (newd, nextp))

print(distance[b])