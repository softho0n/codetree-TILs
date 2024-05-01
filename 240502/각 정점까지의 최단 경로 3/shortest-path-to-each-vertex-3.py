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

INF = 100000000000
distance = [INF] * (n + 1)
distance[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    cur_d, cur_pos = heapq.heappop(q)

    if distance[cur_pos] < cur_d:
        continue
    
    for next_pos, next_d in g[cur_pos]:
        new_distance = cur_d + next_d
        if new_distance < distance[next_pos]:
            distance[next_pos] = new_distance
            heapq.heappush(q, (new_distance, next_pos))

for i in range(2, n+1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])