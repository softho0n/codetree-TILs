import sys

r, c = map(int, sys.stdin.readline().split())
graph = []
for _ in range(r):
    graph.append(list(sys.stdin.readline().split()))

v = [
    [False] * (c)
    for _ in range(r)
]

y, x = 1, 1
cur_c = 'W'
route = [(0, 0)]
answer = 0
def dfs(yy, xx, C):
    for i in range(yy, r):
        for j in range(xx, c):
            if i == r - 1 and j == c - 1:
                if len(route) == 3:
                    global answer
                    answer += 1
                return

            if graph[i][j] != C and v[i][j] is False:
                v[i][j] = True
                route.append((i, j))
                if C == 'W':
                    dfs(i + 1, j + 1, 'B')
                else:
                    dfs(i + 1, j + 1, 'W')
                route.pop()
                v[i][j] = False

dfs(y, x, cur_c)
print(answer)