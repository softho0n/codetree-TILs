import sys



n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


bomb_cnt = 0
b_pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            b_pos.append((i, j))
        
answer = 0

b_type =[
    [0] * n
    for _ in range(n)
]

bomb = [
    [False] * n
    for _ in range(n)
]

def b(i, j, _type):
    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]

    for k in range(5):
        dx, dy = bomb_shapes[_type][k]
        nx, ny = i + dx, j + dy
        
        if ny >= 0 and nx >= 0 and ny < n and nx < n:
            bomb[nx][ny] = True


def calc():
    for i in range(n):
        for j in range(n):
            bomb[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if b_type[i][j] >= 1:
                b(i, j, b_type[i][j])
    
    tmp_cnt = 0
    for i in range(n):
        for j in range(n):
            if bomb[i][j] is True:
                tmp_cnt += 1
    
    global answer
    answer = max(answer, tmp_cnt)

def go(cnt):
    if cnt == len(b_pos):
        calc()
        return
    for k in range(1, 4):
        i, j = b_pos[cnt]
        b_type[i][j] = k
        go(cnt + 1)
        b_type[i][j] = 0

go(0)
print(answer)