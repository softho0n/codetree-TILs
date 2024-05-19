import sys

n = int(input())
edges = [
    []
    for _ in range(n+1)
]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

leaf_nodes = []
for i in range(1, n+1):
    if i == 1:
        continue
    
    if len(edges[i]) == 1:
        leaf_nodes.append(i)

total_length = 0
def go(s, dist, dst, visited):
    if s == dst:
        global total_length
        total_length += dist
        
    for next_pos in edges[s]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            go(next_pos, dist + 1, dst, visited)

for item in leaf_nodes:
    visited = [False for _ in range(n+1)]
    visited[1] = True
    go(1, 0, item, visited)
    
if total_length % 2 == 0:
    print(0)
else:
    print(1)