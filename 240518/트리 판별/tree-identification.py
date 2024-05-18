import sys

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    fa = find_parent(parent, a)
    fb = find_parent(parent, b)

    if fa < fb:
        parent[b] = fa
    else:
        parent[a] = fb

m = int(input())

parent = [0 for _ in range(10001)]
visited = [False for _ in range(10001)]
for i in range(10001):
    parent[i] = i

edges = [
    []
    for _ in range(10001)
]
start = -1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
    start = a
    visited[a] = True
    visited[b] = True
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
    else:
        print(0)
        exit(0)

dfs_visited = [False for _ in range(10001)]
dfs_visited[start] = True
def go(s):
    for next_p in edges[s]:
        if dfs_visited[next_p] is False:
            dfs_visited[next_p] = True
            go(next_p)
go(start)

for i in range(1, 10001):
    if visited[i] != dfs_visited[i]:
        print(0)
        exit(0)
print(1)