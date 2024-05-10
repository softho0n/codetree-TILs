import sys



from collections import deque
n, k = map(int, sys.stdin.readline().split())
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

r1, c1 = map(int, sys.stdin.readline().split())
r2, c2 = map(int, sys.stdin.readline().split())
r1 = r1 - 1
c1 = c1 - 1
r2 = r2 - 1
c2 = c2 - 1

answer = 1000000000
answer_flag = False
def go(cnt):
    if cnt == k:
        q = deque()
        q.append((r1, c1))

        v = [
            [False] * (n + 1)
            for _ in range(n + 1)
        ]
        c = [
            [0] * (n + 1)
            for _ in range(n + 1)
        ]
        v[r1][c1] = True
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]
        while q:
            cy, cx = q.popleft()

            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]

                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                
                if v[ny][nx]:
                    continue
                
                if g[ny][nx] == 0:
                    v[ny][nx] = True
                    c[ny][nx] = c[cy][cx] + 1
                    q.append((ny, nx))
        
        if v[r2][c2] is True:
            global answer
            global answer_flag
            answer_flag = True
            answer = min(answer, c[r2][c2])

        return
    else:
        for i in range(n):
            for j in range(n):
                if g[i][j] == 1:
                    g[i][j] = 0
                    go(cnt + 1)
                    g[i][j] = 1

go(0)

if answer_flag:
    print(answer)
else:
    print(-1)