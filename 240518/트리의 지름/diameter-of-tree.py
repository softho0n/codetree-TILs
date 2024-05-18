import sys
sys.setrecursionlimit(10**9)
n = int(input())
edges = [
    []
    for _ in range(n+1)
]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

visited = [
    False for _ in range(n+1)
]

max_distance = -1
max_pos = -1

def dfs(s, distance):
    global max_distance
    global max_pos
    # print(s, distance)
    if max_distance <= distance:
        max_distance = distance
        max_pos = s

    for next_pos, next_val in edges[s]:
        if visited[next_pos] is False:
            new_distance = distance + next_val
            visited[next_pos] = True
            dfs(next_pos, new_distance)
            # visited[next_pos] = False
visited[1] = True
dfs(1, 0)

visited = [False for _ in range(n+1)]
visited[max_pos] = True
max_distance = -1
dfs(max_pos, 0)
print(max_distance)