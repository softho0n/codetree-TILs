# import sys
# n = int(input())
# sys.setrecursionlimit(n+10)

# edges = [
#     []
#     for _ in range(n+1)
# ]

# for _ in range(n-1):
#     a, b = map(int, sys.stdin.readline().split())
#     edges[a].append(b)
#     edges[b].append(a)

# distance = [-1 for _ in range(n+1)] 
# distance[0] = 0
# distance[1] = 0

# def go(s):
#     visit = False
#     new_dist = distance[s] + 1

#     for new_pos in edges[s]:
#         if distance[new_pos] == -1:
#             distance[new_pos] = new_dist
#             go(new_pos)
#             visit = True
    
#     if visit:
#         distance[s] = 0

# go(1)
# total_length = 0
# for i in range(2, n+1):
#     total_length += distance[i]
    
# if total_length % 2 == 0:
#     print(0)
# else:
#     print(1)

import sys

with open(0) as f:
    n = int(f.readline().strip())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, f.readline().split())
        adj[a].append(b)
        adj[b].append(a)

sys.setrecursionlimit(n + 10)

depths = [None] * (n + 1)
depths[0] = 0
depths[1] = 0

ans = 0
def solve(v):
    # global ans
    visited = False
    dw = depths[v] + 1
    for w in adj[v]:
        if depths[w] is None:
            depths[w] = dw
            solve(w)
            visited = True
    if visited:
        depths[v] = 0
    # else:
    #     ans += depths[v]

solve(1)
ans = 0
for i in range(n + 1):
   ans += depths[i]
print(ans & 1)