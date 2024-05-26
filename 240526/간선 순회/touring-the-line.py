import sys



sys.setrecursionlimit(70000)
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
distance = [0 for _ in range(n + 1)]

def dfs(x, d):
    for next_pos, _ in tree[x]:
        if visited[next_pos]:
            continue
        
        new_dist = d + 1
        distance[next_pos] = new_dist
        visited[next_pos] = True
        dfs(next_pos, new_dist)
visited[2] = True
dfs(2, 0)

max_dist = max(distance)
candidate = []

for i in range(1, n + 1):
    if distance[i] == max_dist:
        candidate.append(i)

def dfs_v2(x, d, rd):

    for next_pos, next_val in tree[x]:
        if visited[next_pos]:
            continue
        next_d = d + 1
        next_rd = rd + next_val
        visited[next_pos] = True
        distance[next_pos] = next_d
        real_distance[next_pos] = next_rd
        dfs_v2(next_pos, next_d, next_rd)

answer = 1000000
for can in candidate:

    visited = [False for _ in range(n + 1)]
    visited[can] = True

    distance = [0 for _ in range(n + 1)]
    real_distance = [0 for _ in range(n + 1)]

    dfs_v2(can, 0, 0)

    second_candidate = []
    second_max = max(distance)
    for i in range(n + 1):
        if distance[i] == second_max:
            second_candidate.append(i)
    
    max_length = []
    for sec_can in second_candidate:
        max_length.append(real_distance[sec_can])

    max_length.sort()
    tmp = max_length[0]

    if tmp % d == 0:
        answer = min(answer, tmp // d)
    else:
        answer = min(answer, (tmp // d) + 1)
    # print(can, max_length)
print(answer)