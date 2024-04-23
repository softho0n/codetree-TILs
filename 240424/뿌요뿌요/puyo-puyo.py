import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [
    [False] * (n + 1)
    for _ in range(n + 1)
]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
tmp_sum = 1
def dfs(y, x, test):
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]

        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        
        if visited[ny][nx]:
            continue
        
        if graph[ny][nx] == test:
            global tmp_sum
            tmp_sum += 1
            visited[ny][nx] = True
            dfs(ny, nx, test)
    
    return tmp_sum
            
bomb_block = 0
max_block_size = 0

for test in range(1, 101):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    phase = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == test and visited[i][j] is False:
                visited[i][j] = True
                tmp_sum = 1
                curr = dfs(i, j, test)

                if curr >= 4:
                    bomb_block += 1
                
                max_block_size = max(max_block_size, curr)

print(bomb_block, max_block_size)