import sys
sys.setrecursionlimit(100005)
n = int(input())

tree = [
    []
    for _ in range(n + 1)
]

visited = [
    False for _ in range(n + 1)
]

dist = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    A, B, C = map(int, sys.stdin.readline().split())
    tree[A].append((B, C))
    tree[B].append((A, C))

last_node = 0
max_dist = 0

def dfs(x):
    global last_node, max_dist
    for next_pos, val in tree[x]:
        if visited[next_pos]:
            continue
        next_dist = dist[x] + val
        dist[next_pos] = next_dist

        if next_dist > max_dist:
            max_dist = next_dist
            last_node = next_pos
        visited[next_pos] = True
        dfs(next_pos)

visited[1] = True
dfs(1)

a = last_node

last_node = 0
max_dist = 0
for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0

visited[a] = True
dfs(a)

b = last_node

for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0

visited[b] = True
visited[a] = True
max_dist = 0
dfs(a)
tmp1 = max_dist


for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0

visited[b] = True
visited[a] = True
max_dist = 0
dfs(b)
tmp2 = max_dist

print(max(tmp1, tmp2))