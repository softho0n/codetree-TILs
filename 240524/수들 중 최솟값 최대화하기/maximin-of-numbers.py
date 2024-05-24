import sys

n = int(input())
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

visited = [False for _ in range(n+1)]

subset = []
answer = -1
def go(row):
    if row == n:
        min_val = min(subset)
        global answer
        answer = max(answer, min_val)
        return
    else:
        for i in range(n):
            if visited[i]:
                continue
            
            visited[i] = True
            subset.append(g[row][i])
            go(row+1)
            subset.pop()
            visited[i] = False

go(0)
print(answer)