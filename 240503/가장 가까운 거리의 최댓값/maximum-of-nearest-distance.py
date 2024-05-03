import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
a, b, c = map(int, sys.stdin.readline().split())

g = [
    []
    for _  in range(n+1)
]

for _ in range(m):
    s, t, d = map(int, sys.stdin.readline().split())
    g[s].append((t, d))
    g[t].append((s, d))

INF = 100000000000
abc_list = [INF] * (n + 1)

def d(k):
    q = []
    distance = [INF] * (n + 1)
    distance[k] = 0
    heapq.heappush(q, (0, k))

    while q:
        curd, curp = heapq.heappop(q)

        if distance[curp] < curd:
            continue
        
        for np, nd in g[curp]:
            newd = curd + nd
            if newd < distance[np]:
                distance[np] = newd
                heapq.heappush(q, (newd, np))
    
    for i in range(1, n+1):
        abc_list[i] = min(abc_list[i], distance[i])

d(a)
d(b)
d(c)

ans = 0
for i in range(1, n+1):
    ans = max(ans, abc_list[i])

print(ans)