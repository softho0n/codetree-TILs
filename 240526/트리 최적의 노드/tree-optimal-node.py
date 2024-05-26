import sys

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
max_node = -1
max_length = -1
for i in range(1, n + 1):
    if len(tree[i]) > max_length:
        max_length = len(tree[i])
        max_node = i

visited = [False for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]

def get_maximum_distance(s, d):
    for next_pos in tree[s]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            distance[next_pos] = d + 1
            get_maximum_distance(next_pos, d + 1)


# print(max_node)
answer = 100000000000
# for i in range(1, n+1):
visited = [False for _ in range(n+1)]
visited[max_node] = True
get_maximum_distance(max_node, 0)
tmp_answer = max(distance)
answer = min(answer, tmp_answer)
# print(distance[:n+1])
print(answer)