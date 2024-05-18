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

out = [
    []
    for _ in range(10001)
]

_in = [
    []
    for _ in range(10001)
]

start = -1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    visited[a] = True
    visited[b] = True
    _in[b].append(a)
    out[a].append(b)

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
    else:
        print(0)
        exit(0)

root_cnt = 0
root = 0
for i in range(1, 10001):
    if visited[i] is True:
        if len(_in[i]) == 0:
            root_cnt += 1
            root = i

if root_cnt >= 2:
    print(0)

# dfs_visited = [False for _ in range(10001)]
# dfs_visited[root] = True
# def go(s):
#     for np in out[s]:
#         if dfs_visited[np] is False:
#             dfs_visited[np] = True
#             go(np)
# go(root)

# for i in range(10001):
#     if visited[i] != dfs_visited[i]:
#         print(0)
#         exit(0)

print(1)