import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
a_g = [[] for _ in range(n + 1)]
b_g = [[] for _ in range(n + 1)]
ra_g = [[] for _ in range(n + 1)]
rb_g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a_g[a].append((b, c))
    ra_g[b].append((a, c))

    b_g[a].append((b, d))
    rb_g[b].append((a, d))

def d(distance, g):
    q = []
    heapq.heappush(q, (0, n))

    distance[n] = 0

    while q:
        cd, cp = heapq.heappop(q)

        if distance[cp] < cd:
            continue
        
        for np, nd in g[cp]:
            newd = nd + cd
            if newd < distance[np]:
                distance[np] = newd
                heapq.heappush(q, (newd, np))
INF = 100000000
a_dist = [INF] * (n + 1)
b_dist = [INF] * (n + 1)

d(a_dist, ra_g)
d(b_dist, rb_g)

def answer_d(distance, ag, bg, bak_ad, bak_bd):
    q = []
    heapq.heappush(q, (0, 1))

    distance[1] = 0

    while q:
        cd, cp = heapq.heappop(q)

        if distance[cp] < cd:
            continue
        
        l = len(ag[cp])
        for i in range(l):
            at, av = ag[cp][i]
            bt, bv = bg[cp][i]

            task = 0
            if bak_ad[cp] != bak_ad[at] + av:
                task += 1
            if bak_bd[cp] != bak_bd[bt] + bv:
                task += 1
            
            newd = cd + task
            if newd < distance[at]:
                distance[at] = newd
                heapq.heappush(q, (newd, at))

d = [INF] * (n + 1)
answer_d(d, a_g, b_g, a_dist, b_dist)
print(d[n])