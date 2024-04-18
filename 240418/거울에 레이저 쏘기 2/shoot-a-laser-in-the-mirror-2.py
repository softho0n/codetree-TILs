import sys
n = int(input())
graph = []

for _ in range(n):
    graph.append(
        list(sys.stdin.readline().rstrip())
    )

k = int(input())
k = k - 1
cur_d = k // n
x = k %  n

candidate = []
for i in range(n):
    candidate.append((0, i))

for i in range(n):
    candidate.append((i, n-1))

for i in range(n):
    candidate.append((n-1, n-i-1))

for i in range(n):
    candidate.append((n-i-1, 0))

y = candidate[k][0]
x = candidate[k][1]
ny, nx = y, x

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

answer = 0
while True:
    if ny < 0 or nx < 0 or ny >= n or nx >= n:
        break

    if graph[ny][nx] == '/':
        if cur_d == 0:
            cur_d = 1
        elif cur_d == 3:
            cur_d = 2
        elif cur_d == 2:
            cur_d = 3
        elif cur_d == 1:
            cur_d = 0
        answer += 1
        ny, nx = ny + dy[cur_d], nx + dx[cur_d]
    else:
        if cur_d == 0:
            cur_d = 3
        elif cur_d == 3:
            cur_d = 0
        elif cur_d == 2:
            cur_d = 1
        elif cur_d == 1:
            cur_d = 2
        answer += 1
        ny, nx = ny + dy[cur_d], nx + dx[cur_d]

print(answer)