import sys
n, m = map(int, sys.stdin.readline().split())
edges = [
    []
    for _ in range(n+1)
]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

def go(s, distance, visited, dst):
    # # if s == dst:
    # #     return distance
    # print(s)
    if s == dst:
        print(distance)
    for next_pos, val in edges[s]:
        if visited[next_pos] is False:
            new_distance = val + distance
            visited[next_pos] = True
            go(next_pos, new_distance, visited, dst)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(n + 1)]
    visited[a] = True
    ans = go(a, 0, visited, b)
    # print(ans)