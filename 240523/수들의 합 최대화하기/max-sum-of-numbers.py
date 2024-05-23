import sys

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

row_visited = [False for _ in range(n)]
col_visited = [False for _ in range(n)]

subset = []
answer = 0
def calc():
    tmp = 0
    for x, y in subset:
        tmp += graph[x][y]
    global answer
    answer = max(answer, tmp)

def go2(row):
    if row == n:
        calc()
        return
    else:
        for i in range(n):
            if col_visited[i]:
                continue
            col_visited[i] = True
            subset.append((row, i))
            go2(row+1)
            subset.pop()
            col_visited[i] = False

def go(cnt):
    if cnt == n:
        calc()
        return
    else:
        for i in range(n):
            for j in range(n):
                if row_visited[i]:
                    continue
                if col_visited[j]:
                    continue
                
                row_visited[i] = True
                col_visited[j] = True
                subset.append((i, j))
                go(cnt + 1)
                subset.pop()
                row_visited[i] = False
                col_visited[j] = False

go2(0)
print(answer)