import sys
import heapq


sys.setrecursionlimit(100000)
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
q = []
def dfs(x, d, rd):
    for next_pos, next_val in tree[x]:
        if visited[next_pos]:
            continue
        
        new_dist = d + 1
        new_rd = rd + next_val
        
        heapq.heappush(q, (-new_dist, new_rd, next_pos))
        visited[next_pos] = True
        dfs(next_pos, new_dist, new_rd)

visited[2] = True
dfs(2, 0, 0)
visited = [False for _ in range(n + 1)]

Z, A, POS = heapq.heappop(q)
visited[POS] = True
q.clear()
def dfs_v2(x, d, rd):
    for next_pos, next_val in tree[x]:
        if visited[next_pos]:
            continue
        next_d = d + 1
        next_rd = rd + next_val
        # print(x, next_pos, rd, next_val, next_d)
        visited[next_pos] = True
        heapq.heappush(q, (-next_d, next_rd, next_pos))
        # distance[next_pos] = next_d
        # real_distance[next_pos] = next_rd
        dfs_v2(next_pos, next_d, next_rd)
# print(POS)
dfs_v2(POS, 0, 0)
level, tmp, _ = heapq.heappop(q)
answer = 10000000
q.clear()
if tmp % d == 0:
    answer = min(answer, tmp // d)
else:
    answer = min(answer, (tmp // d) + 1)
    
print(answer)
# answer = 1000000
# for _, can in candidate:

#     visited = [False for _ in range(n + 1)]
#     visited[can] = True

#     distance = [0 for _ in range(n + 1)]
#     real_distance = [0 for _ in range(n + 1)]

#     dfs_v2(can, 0, 0)

#     second_candidate = []
#     second_max = max(distance)
#     for i in range(n + 1):
#         if distance[i] == second_max:
#             second_candidate.append(i)
    
#     max_length = []
#     for sec_can in second_candidate:
#         max_length.append(real_distance[sec_can])

#     max_length.sort()
#     tmp = max_length[0]


#     # print(can, max_length)
# print(answer)