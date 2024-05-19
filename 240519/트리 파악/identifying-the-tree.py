import sys
sys.setrecursionlimit(10**5)
n = int(input())
edges = [
    []
    for _ in range(n+1)
]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

distance = [-1 for _ in range(n+1)] 
distance[0] = 0
distance[1] = 0

def go(s, dist):
    visit = False
    new_dist = dist + 1

    for new_pos in edges[s]:
        if distance[new_pos] == -1:
            distance[new_pos] = new_dist
            go(new_pos, new_dist)
            visit = True
    
    if visit:
        distance[s] = 0

go(1, 0)
total_length = 0
for i in range(2, n+1):
    total_length += distance[i]
    
if total_length % 2 == 0:
    print(0)
else:
    print(1)