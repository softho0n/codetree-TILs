import sys
n, m = map(int, sys.stdin.readline().split())
al = []
for _ in range(n):
    al.append(
        list(sys.stdin.readline().rstrip())
    )
bl = []
for _ in range(n):
    bl.append(
        list(sys.stdin.readline().rstrip())
    )

answer = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            As = set()
            Bs = set()
            for p in range(n):
                As.add("".join([al[p][i], al[p][j], al[p][k]]))
                Bs.add("".join([bl[p][i], bl[p][j], bl[p][k]]))
            
            As = list(As)
            flag = True
            for item in As:
                if item in Bs:
                    flag = False
                    break
            
            if flag:
                answer += 1

print(answer)