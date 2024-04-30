import sys

n, m = map(int, sys.stdin.readline().split())
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))


ptn1 = []
ptn2 = []
answer = -10000000000

def can():
    xp1 = [ptn1[0][0], ptn1[1][0]]
    yp1 = [ptn1[0][1], ptn1[1][1]]

    xp2 = [ptn2[0][0], ptn2[1][0]]
    yp2 = [ptn2[0][1], ptn2[1][1]]

    xp1.sort()
    yp1.sort()
    xp2.sort()
    yp2.sort()
    
    v = [
        [False] * n
        for _ in range(n)
    ]

    s1 = 0
    for i in range(xp1[0], xp1[1]+1):
        for j in range(yp1[0], yp1[1]+1):
            v[i][j] = True
            s1 += g[i][j]
    
    s2 = 0
    for i in range(xp2[0], xp2[1]+1):
        for j in range(yp2[0], yp2[1]+1):
            if v[i][j]:
                return False
            else:
                v[i][j] = True
                s2 += g[i][j]
    s3 = s1 + s2
    global answer
    answer = max(answer, s3)
    return True


    


def go(cnt1, cnt2):
    if cnt1 == 2 and cnt2 == 2:
        can()
        return
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for p in range(n):
                        ptn1.append((i, j))
                        ptn2.append((k, p))
                        go(cnt1+1, cnt2+1)
                        ptn1.pop()
                        ptn2.pop()

go(0, 0)
print(answer)