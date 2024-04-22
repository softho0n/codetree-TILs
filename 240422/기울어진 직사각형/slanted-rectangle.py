import sys

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


dys = [-1, -1, 1, 1]
dxs = [1, -1, -1, 1]
answer = 0

def calc(x, y, k, l):
    move_pattern = [k, l, k, l]

    tmp_sum = 0
    for dy, dx, move in zip(dys, dxs, move_pattern):
        for _ in range(move):
            x = x + dx
            y = y + dy

            if x < 0 or y < 0 or x >= n or y >= n:
                return 0

            tmp_sum += graph[x][y]

    global answer
    answer = max(answer, tmp_sum)

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                calc(i, j, k, l)

print(answer)