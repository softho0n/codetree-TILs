import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(
        map(int, sys.stdin.readline().split())
    ))

visited = [
    [False] * m
    for _ in range(n)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def can_go(y, x):
    if y < 0 or x < 0 or y >= n or x >= m:
        return False
    return True

def fill_ice():
    for i in range(n):
        for j in range(m):
            if visited[i][j] is False and graph[i][j] == 0:
                y = i
                x = j
                break
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    
    graph[y][x] = 3
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if can_go(ny, nx) and visited[ny][nx] is False and graph[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = True
                graph[ny][nx] = 3

def verify_ice(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if can_go(ny, nx) and graph[ny][nx] == 3:
            return True
    return False

def printMap():
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=' ')
        print()
    print()

def b_ice():
    candidate = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] == 1 and verify_ice(i, j):
                visited[i][j] = True
                candidate.append((i, j))
    return candidate

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0 and visited[i][j] is False:
#             fill_ice(i, j)
        
#         if graph[i][j] == 1 and visited[i][j] is False:
#             ice_candidate = break_ice(i, j)

#             for iy, ix in ice_candidate:
#                 graph[iy][ix] = 3
            
#             printMap()

cnt = 0
answer = -1
while True:
    fill_ice()
    candidate = b_ice()
    if len(candidate) == 0:
        break
    
    for iy, ix in candidate:
        graph[iy][ix] = 3
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 3:
                graph[i][j] = 0
                visited[i][j] = False

    answer = len(candidate)
    cnt += 1
print(cnt, answer)