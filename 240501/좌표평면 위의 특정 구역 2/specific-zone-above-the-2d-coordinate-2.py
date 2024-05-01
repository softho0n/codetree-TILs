import sys

n = int(input())
ptns = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptns.append((x, y))

answer = 1800000000
for i in range(n):

    xs = []
    ys = []

    for j in range(n):
        if i == j:
            continue
        
        cx, cy = ptns[j]
        xs.append(cx)
        ys.append(cy)
    
    xs.sort()
    ys.sort()

    tmp = abs(xs[-1] - xs[0]) * abs(ys[-1] - ys[0])
    answer = min(answer, tmp)

print(answer)