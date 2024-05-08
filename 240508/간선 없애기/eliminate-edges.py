import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
info = []

graph = [
    []
    for _ in range(n + 1)
]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    info.append((a, b, c))

INF = 40000
distance = [INF] * (n + 1)
distance[1] = 0

q = []
route = [0] * (n + 1)
heapq.heappush(q, (0, 1))

while q:
    cd, cp = heapq.heappop(q)

    if distance[cp] < cd:
        continue
    
    for np, nd in graph[cp]:
        newd = nd + cd
        if newd < distance[np]:
            distance[np] = newd
            route[np] = cp
            heapq.heappush(q, (newd, np))

original = distance[n]
x = n
path = [x]
while x != 1:
    x = route[x]
    path.append(x)
path = path[::-1]

answer = 0

for i in range(len(path) - 1):
    c1, c2 = path[i], path[i+1]
    graph = [
        []
        for _ in range(n + 1)
    ]
    
    for j in range(m):
        ca, cb, cc = info[j]

        if (c1, c2) == (ca, cb) or (c2, c1) == (ca, cb):
            continue
        else:
            graph[ca].append((cb, cc))
            graph[cb].append((ca, cc))
    
    INF = 40000
    distance = [INF] * (n + 1)
    distance[1] = 0

    q = []
    heapq.heappush(q, (0, 1))

    while q:
        cd, cp = heapq.heappop(q)

        if distance[cp] < cd:
            continue
        
        for np, nd in graph[cp]:
            newd = nd + cd
            if newd < distance[np]:
                distance[np] = newd
                route[np] = cp
                heapq.heappush(q, (newd, np))


    if original != distance[n]:
        answer += 1

print(answer)