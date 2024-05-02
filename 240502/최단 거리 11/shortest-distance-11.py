import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
g = [
    [0] * (n + 1)
    for _ in range(n+1)
]
for _ in range(m):
    s, t, d = map(int, sys.stdin.readline().split())
    # g[s].append((t, d))
    g[s][t] = d
    g[t][s] = d
    # g[t].append((s, d))

a, b = map(int, sys.stdin.readline().split())
INF = 100000000
distance = [INF] * (n + 1)
distance[b] = 0

q = []
heapq.heappush(q, (0, b))

while q:
    curd, curp = heapq.heappop(q)

    if distance[curp] < curd:
        continue
    
    for i in range(1, n+1):
        if g[curp][i] != 0:
            nextd = g[curp][i]
            newd = nextd + curd
            if newd < distance[i]:
                distance[i] = newd
                heapq.heappush(q, (newd, i))

print(distance[a])

x = a
route = [a]
while x!=b:
    for i in range(n+1):
        if g[x][i] == 0:
            continue
        
        if distance[x] == distance[i] + g[x][i]:
            route.append(i)
            x = i
            break



print(*route)