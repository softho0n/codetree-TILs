import sys
sys.setrecursionlimit(10**5+14)
n = int(input())
edges = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
s = 1
first_node = -1
first_max = -1
visited = [False for _ in range(n+1)]
def go(s, dist):
    global first_max
    global first_node
    if first_max < dist:
        first_max = dist
        first_node = s

    for next_pos, val in edges[s]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            go(next_pos, dist+val)
visited[1] = True
go(1, 0)
visited = [False for _ in range(n+1)]
second_max = -1
def go2(s, dist):
    global second_max
    if second_max < dist:
        second_max = dist

    for next_pos, val in edges[s]:
        if visited[next_pos] is False:
            visited[next_pos] = True
            go2(next_pos, dist+val)
visited[first_node] = True
go2(first_node, 0)
# print(first_node, first_max)
print(second_max)