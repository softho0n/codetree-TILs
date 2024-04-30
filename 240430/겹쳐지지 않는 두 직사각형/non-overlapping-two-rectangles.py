import sys

n, m = map(int, sys.stdin.readline().split())
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))


ptn1 = []
ptn2 = []
answer = -10000000000

def can():
    xx = [ptn1[0], ptn1[1]]
    xx.sort()
    yy = [ptn2[0], ptn2[1]]
    yy.sort()

    v = [
        [False] * n
        for _ in range(n)
    ]

    s1 = 0
    for i in range(xx[0][0], xx[1][0]+1):
        for j in range(xx[0][1], xx[1][1]+1):
            v[i][j] = True
            s1 += g[i][j]
    
    s2 = 0
    for i in range(yy[0][0], yy[1][0]+1):
        for j in range(yy[0][1], yy[1][1]+1):
            if v[i][j]:
                return False
            else:
                v[i][j] = True
                s2 += g[i][j]
    s3 = s1 + s2
    global answer
    answer = max(answer, s3)
    return True


    


def go(cnt1, cnt2, ii, jj, kk, pp):
    if cnt1 == 2 and cnt2 == 2:
        can()
        return
    else:
        for i in range(ii, n):
            for j in range(jj, n):
                for k in range(kk, n):
                    for p in range(pp, n):
                        ptn1.append((i, j))
                        ptn2.append((k, p))
                        go(cnt1+1, cnt2+1, i, j, k, p)
                        ptn1.pop()
                        ptn2.pop()

go(0, 0, 0, 0, 0, 0)
print(answer)