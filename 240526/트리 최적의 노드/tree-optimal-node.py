import sys
sys.setrecursionlimit(100004)
n = int(input())
tree = [
    []
    for _ in range(n+1)
]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    
    tree[a].append(b)
    tree[b].append(a)

# 루트 노드의 조건 -> 들어오는건 없어야하고 
# print(tree)

visited = [False for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
def dfs(x, d):
    for next_pos in tree[x]:
        if visited[next_pos]:
            continue

        distance[next_pos] = d + 1
        visited[next_pos] = True
        dfs(next_pos, d + 1)

visited[1] = True
dfs(1, 0)
max_dist = -1
last_idx = -1
answer = 0
for i in range(n + 1):
    if distance[i] > max_dist:
        max_dist = distance[i]
        last_idx = i

answer += max_dist
visited = [False for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
dfs(last_idx, 0)
max_dist = -1
last_idx = -1
for i in range(n + 1):
    if distance[i] > max_dist:
        max_dist = distance[i]
        last_idx = i

print((max_dist + 1) // 2)