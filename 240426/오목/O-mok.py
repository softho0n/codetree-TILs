import sys

graph = []
for _ in range(19):
    graph.append(
        list(map(int, sys.stdin.readline().split()))
    )

def verify(y, x, b):
    tmp_sum = 0
    c = [(y, x)]
    for i in range(y-4, y):
        if i >= 0:
            if graph[i][x] == b:
                c.append((i, x))
                tmp_sum += 1
    
    if tmp_sum == 4:
        return c
    
    c = [(y, x)]
    tmp_sum = 0
    for i in range(y+1,y+5):
        if i < 19:
            if graph[i][x] == b:
                c.append((i, x))
                tmp_sum += 1
    if tmp_sum == 4:
        return c
    
    tmp_sum = 0
    c = [(y, x)]
    for j in range(x+1, x+5):
        if j < 19:
            if graph[y][j] == b:
                c.append((y, j))
                tmp_sum += 1
    if tmp_sum == 4:
        return c
    
    tmp_sum = 0
    c = [(y, x)]
    for j in range(x-4, x):
        if j >= 0:
            if graph[y][j] == b:
                tmp_sum += 1
                c.append((y, j))
    if tmp_sum == 4:
        return c
    
    tmp_sum = 0
    dy = [1, 2, 3, 4]
    dx = [1, 2, 3, 4]
    c = [(y, x)]
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if ny < 19 and nx < 19:
            if graph[ny][nx] == b:
                c.append((ny, nx))
                tmp_sum += 1

    if tmp_sum == 4:
        return c
    
    tmp_sum = 0
    dy = [-1, -2, -3, -4]
    dx = [1, 2, 3, 4]
    c = [(y, x)]
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if ny >= 0 and nx < 19:
            if graph[ny][nx] == b:
                tmp_sum += 1
                c.append((ny, nx))

    if tmp_sum == 4:
        return c
    
    tmp_sum = 0
    dy = [-1, -2, -3, -4]
    dx = [-1, -2, -3, -4]
    c = [(y, x)]
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if ny >= 0 and nx >= 0:
            if graph[ny][nx] == b:
                c.append((ny, nx))
                tmp_sum += 1

    if tmp_sum == 4:
        return c

    tmp_sum = 0
    dy = [1, 2, 3, 4]
    dx = [-1, -2, -3, -4]
    c = [(y, x)]
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if ny < 19 and nx >= 0:
            if graph[ny][nx] == b:
                c.append((ny, nx))
                tmp_sum += 1

    if tmp_sum == 4:
        return c

    c = []
    return c

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            b = verify(i, j, graph[i][j])
            if len(b) == 5:
                print(graph[i][j])
                print(b[2][0]+1, b[2][1]+1)
                exit(0)

print(0)