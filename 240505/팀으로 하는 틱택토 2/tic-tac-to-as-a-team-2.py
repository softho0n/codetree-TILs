import sys


g = []
for _ in range(3):
    k  = list(sys.stdin.readline().rstrip())
    k = [int(item) for item in k]
    g.append(k)

cnt = 0
solution = []
for i in range(3):
    row = g[i]
    s = set(row)
    s = list(s)
    s.sort()
    if len(s) == 2 and not s in solution:
        solution.append(s)
        cnt += 1

for j in range(3):
    tmp = []
    for i in range(3):
        tmp.append(g[i][j])
    
    s = set(tmp)
    s = list(s)
    s.sort()
    if len(s) == 2 and not s in solution:
        cnt += 1
        solution.append(s)

s = set([g[0][0], g[1][1], g[2][2]])
s = list(s)
s.sort()
if len(s) == 2 and not s in solution:
    cnt += 1
    solution.append(s)

s = set([g[0][2], g[1][1], g[2][0]])
s = list(s)
s.sort()
if len(s) == 2 and not s in solution:
    cnt += 1
    solution.append(s)

print(cnt)