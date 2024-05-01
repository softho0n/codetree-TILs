import sys

n, m = map(int, sys.stdin.readline().split())
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

ptns = []
answer = 0

def calc():
    y = [ptns[0][0], ptns[1][0]]
    x = [ptns[0][1], ptns[1][1]]
    y.sort()
    x.sort()

    flag = True
    cnt = 0
    for i in range(y[0], y[1]+1):
        for j in range(x[0], x[1]+1):
            if g[i][j] <= 0:
                flag = False
                break
            else:
                cnt += 1
    
    if flag:
        global answer
        answer = max(answer, cnt)


def go(cnt):
    if cnt == 2:
        calc()
        return
    else:
        for i in range(n):
            for j in range(m):
                ptns.append((i, j))
                go(cnt + 1)
                ptns.pop()

go(0)
if answer == 0:
    print(-1)
else:
    print(answer)