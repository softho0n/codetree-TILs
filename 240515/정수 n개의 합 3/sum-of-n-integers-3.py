import sys

n, k = map(int, sys.stdin.readline().split())
k -= 1
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

g.insert(0, [0 for _ in range(n)])
for i in range(n+1):
    g[i].insert(0, 0)

ps = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n+1):
    for j in range(1, n+1):
        ps[i][j] = g[i][j] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i + k <= n and j + k <= n:
            tmp_sum = ps[i+k][j+k] + ps[i-1][j-1] - ps[i+k][j-1] - ps[i-1][j+k]
            answer = max(answer, tmp_sum)
print(answer)