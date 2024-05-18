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
edges = [
    []
    for _ in range(m+1)
]

parent = [0 for _ in range(10001)]
for i in range(10001):
    parent[i] = i

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # edges[a].append(b)
    # edges[b].append(a)

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
    else:
        print(0)
        exit(0)

print(1)