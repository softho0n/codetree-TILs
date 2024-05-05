import sys


g = []
for _ in range(3):
    k  = list(sys.stdin.readline().rstrip())
    k = [int(item) for item in k]
    g.append(k)

cnt = 0
for i in range(3):
    row = g[i]
    s = set(row)
    s = list(s)
    if len(s) == 2:
        cnt += 1

for j in range(3):
    tmp = []
    for i in range(3):
        tmp.append(g[i][j])
    
    s = set(tmp)
    s = list(s)
    if len(s) == 2:
        cnt += 1

s = set([g[0][0], g[1][1], g[2][2]])
s = list(s)
if len(s) == 2:
    cnt += 1

s = set([g[0][2], g[1][1], g[2][0]])
s = list(s)
if len(s) == 2:
    cnt += 1

print(cnt)