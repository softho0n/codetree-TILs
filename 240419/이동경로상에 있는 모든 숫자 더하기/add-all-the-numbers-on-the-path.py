import sys



n, t = map(int, sys.stdin.readline().split())
cmd = list(sys.stdin.readline().rstrip())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

y, x = n // 2, n // 2
# 북, 서, 남, 동
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
curd = 0

answer = graph[y][x]

for i in range(t):
    if cmd[i] == 'R':
        # 0 -> 3
        # 1 -> 0
        # 2 -> 1
        # 3 -> 2
        curd = (curd - 1) % 4
    elif cmd[i] == 'L':
        curd = (curd + 1) % 4
    elif cmd[i] == 'F':
        ny, nx = y + dy[curd], x + dx[curd]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        
        answer += graph[ny][nx]
        y, x = ny, nx
print(answer)