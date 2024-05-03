import sys
import heapq
n, a, b = map(int, sys.stdin.readline().split())
g = [

]

for _ in range(n):
    s = list(sys.stdin.readline().rstrip())
    g.append(s)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = 0

for i in range(n):
    for j in range(n):

        for k in range(i+1, n):
            for p in range(j+1, n):
                
                INF = 100000000
                distance = [
                    [INF] * (n + 1)
                    for _ in range(n + 1)
                ]
                visited = [
                    [False] * (n + 1)
                    for _ in range(n + 1)
                ]
                distance[i][j] = 0
                visited[i][j] = True
                q = []
                heapq.heappush(q, (0, (i, j)))

                while q:
                    curd, curtuple = heapq.heappop(q)
                    cy, cx = curtuple

                    if cy == k and cx == p:
                        answer = max(answer, curd)

                    for z in range(4):
                        ny, nx = cy + dy[z], cx + dx[z]

                        if ny < 0 or nx < 0 or ny >= n or nx >= n:
                            continue
                        
                        if visited[ny][nx]:
                            continue
                        
                        if g[cy][cx] != g[ny][nx]:
                            heapq.heappush(q, (curd + b, (ny, nx)))
                        else:
                            heapq.heappush(q, (curd + a, (ny, nx)))
                        
                        visited[ny][nx] = True

print(answer)