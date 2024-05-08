import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
graph = [
    []
    for _ in range(n + 1)
]

aa = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    aa.append((a, b, c))

INF = 10000000000
distance = [INF] * (n + 1)
distance[1] = 0
route = [0] * (n + 1)
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

path = [n]
x = n
while x!=1:
    x = route[x]
    path.append(x)

path = path[::-1]
original_min = distance[n]
# print(*distance)
# print(*path)

answer = 0
for i in range(len(path) - 1):
    x1, x2 = path[i], path[i+1]

    graph = [
        []
        for _ in range(n + 1)
    ]

    for a, b, c in aa:
        if (x1, x2) == (a, b) or (x2, x1) == (a, b):
            graph[a].append((b, c * 2))
            graph[b].append((a, c * 2))
        else:
            graph[a].append((b, c))
            graph[b].append((a, c))
    

    INF = 10000000000
    distance_t = [INF] * (n + 1)
    distance_t[1] = 0
    q = []
    heapq.heappush(q, (0, 1))


    while q:
        cd, cp = heapq.heappop(q)
        if distance_t[cp] < cd:
            continue
        
        for np, nd in graph[cp]:
            newd = nd + cd
            if newd < distance_t[np]:
                distance_t[np] = newd
                heapq.heappush(q, (newd, np))
    
    answer = max(answer, distance_t[n] - original_min)

print(answer)