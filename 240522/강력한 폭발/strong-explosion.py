import sys
n = int(input())
bomb = [
    [False] * (n + 1)
    for _ in range(n + 1)
]
graph = []
for _ in range(n):
    graph.append(
        list(map(int, sys.stdin.readline().split()))
    )

bomb_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bomb_pos.append((i, j))

answer = 0
def b(i, j, t):
    if t == 2:
        dy = [-2, -1, 0, 1, 2]
        dx = [0, 0, 0, 0, 0]
        for p in range(5):
            ny, nx = i + dy[p], j + dx[p]
            if ny >= 0 and nx >= 0 and ny < n and nx < n:
                bomb[ny][nx] = True
    elif t == 3:
        dy = [0, -1, 0, 1, 0]
        dx = [0, 0, 1, 0, -1]
        for p in range(5):
            ny, nx = i + dy[p], j + dx[p]
            if ny >= 0 and nx >= 0 and ny < n and nx < n:
                bomb[ny][nx] = True
    elif t == 4:
        dy = [0, -1, -1, 1, 1]
        dx = [0, -1, 1, 1, -1]
        for p in range(5):
            ny, nx = i + dy[p], j + dx[p]
            if ny >= 0 and nx >= 0 and ny < n and nx < n:
                bomb[ny][nx] = True

def calc():
    for i in range(n):
        for j in range(n):
            bomb[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2:
                b(i, j, graph[i][j])

    tmp_sum = 0
    for i in range(n):
        for j in range(n):
            # print(bomb[i][j], end=' ')
            if bomb[i][j] is True:
                tmp_sum += 1
        # print()
    # print()
    global answer
    answer = max(answer, tmp_sum)

def go(cnt):
    if cnt == len(bomb_pos):
        # for i in range(n):
        #     for j in range(n):
        #         print(graph[i][j], end=' ')
        #     print()
        # print()
        calc()
        return
    else:
        x, y = bomb_pos[cnt]
        for j in range(2, 5):
            graph[x][y] = j
            go(cnt + 1)
            graph[x][y] = 1

go(0)
print(answer)