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

visited = [False for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]

def get_maximum_distance(s, d):
    for next_pos in tree[s]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            distance[next_pos] = d + 1
            get_maximum_distance(next_pos, d + 1)


answer = 100000000000
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    visited[i] = True
    get_maximum_distance(i, 0)
    tmp_answer = max(distance)
    answer = min(answer, tmp_answer)
print(answer)