import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
k = int(input())
g = [
    []
    for _ in range(n+1)
]

for _ in range(m):
    s, t, d = map(int, sys.stdin.readline().split())
    g[s].append((t, d))
    g[t].append((s, d))

INF = 10000000000
distance = [INF] * (n + 1)
distance[k] = 0

q = []
heapq.heappush(q, (0, k))

while q:
    cur_d, cur_p = heapq.heappop(q)

    if distance[cur_p] < cur_d:
        continue
    
    for next_pos, next_d in g[cur_p]:
        new_distance = next_d + cur_d
        if new_distance < distance[next_pos]:
            distance[next_pos] = new_distance
            heapq.heappush(q, (new_distance, next_pos))

for i in range(1, n+1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])