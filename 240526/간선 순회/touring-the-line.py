import sys
import heapq


sys.setrecursionlimit(100000)
n, d = map(int, sys.stdin.readline().split())
tree = [
    []
    for _ in range(n + 1)
]

for _ in range(n-1):
    a, b, c= map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [False for _ in range(n + 1)]
dist_node = [0 for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]

last_node = 0
max_dist = (0, 0)

def dfs(x):
    global last_node, max_dist

    for next_pos, next_val in tree[x]:
        if visited[next_pos]:
            continue
        
        next_dist_node = dist_node[x] + 1
        next_dist = dist[x] + next_val
        visited[next_pos] = True

        dist_node[next_pos] = next_dist_node
        dist[next_pos] = next_dist

        if max_dist < (next_dist_node, -next_dist):
            max_dist = (next_dist_node, -next_dist)
            last_node = next_pos

        dfs(next_pos)

visited[1] = True
dfs(1)

for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0
    dist_node[i] = 0


visited[last_node] = True
dfs(last_node)

print(1 + (-max_dist[1] - 1) // d)