import sys

n = int(input())
edges = [
    []
    for _ in range(100001)
]
parents = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

def go(s):
    for next_pos in edges[s]:
        if visited[next_pos] is False:
            parents[next_pos] = s
            visited[next_pos] = True
            go(next_pos)

go(1)
for i in range(2, n+1):
    print(parents[i])