import heapq
import sys

n, m = map(int, sys.stdin.readline().split())

g = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a][b] = c
    g[b][a] = c

INF = 10000000
distance = [INF] * (n + 1)
distance[n] = 0

q = []
heapq.heappush(q, (0, n))

while q:
    cd, cp = heapq.heappop(q)

    if distance[cp] < cd:
        continue
    
    for i in range(1, n+1):
        if g[cp][i] > 0:
            newd = cd + g[cp][i]
            if newd < distance[i]:
                distance[i] = newd
                heapq.heappush(q, (newd, i))
    
x = 1
path = [x]

while x != n:
    for i in range(1, n+1):
        if distance[i] >= INF:
            continue
        if i == x:
            continue
        if g[x][i] == 0:
            continue
            
        if distance[x] == g[x][i] + distance[i]:
            x = i
            path.append(x)
            break
        
a_path = []
for i in range(len(path) - 1):
    a_path.append((path[i], path[i+1]))

INF = 10000000
distance = [INF] * (n + 1)
distance[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    cd, cp = heapq.heappop(q)

    if distance[cp] < cd:
        continue
    
    for i in range(1, n+1):
        if (cp, i) in a_path:
            continue
        if g[cp][i] > 0:
            newd = cd + g[cp][i]
            if newd < distance[i]:
                distance[i] = newd
                heapq.heappush(q, (newd, i))

if distance[n] == INF:
    print(-1)
else:
    print(distance[n])