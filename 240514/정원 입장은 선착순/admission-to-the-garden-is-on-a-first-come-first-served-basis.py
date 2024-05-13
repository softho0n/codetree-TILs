import sys
import heapq

n = int(input())
p = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

for i in range(n):
    p[i].insert(0, i)

p.sort(key=lambda x: x[1])
w = [0] * (n + 1)
exit_time = 0
pq = []

for i in range(n):
    idx, at, dt = p[i]

    while at > exit_time and pq:
        cur_idx, cur_at, cur_dt = heapq.heappop(pq)
        w[cur_idx] = exit_time - cur_at
        exit_time += cur_dt

    if at > exit_time:
        w[idx] = 0
        exit_time = at + dt
    else:
        heapq.heappush(pq, (idx, at, dt))

while pq:
    cur_idx, cur_at, cur_dt = heapq.heappop(pq)
    w[cur_idx] = exit_time - cur_at
    exit_time += cur_dt

print(max(w))