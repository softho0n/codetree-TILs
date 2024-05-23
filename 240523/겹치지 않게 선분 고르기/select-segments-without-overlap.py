import sys
n = int(input())
p = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    p.append((x, y))

p.sort()
subset = []

answer = 0

def calc():
    if len(subset) == 0:
        return
    
    x0, y0 = subset[0]
    tmp = 1
    for i in range(1, len(subset)):
        cx, cy = subset[i]
        if y0 < cx:
            tmp += 1
            y0 = cx
    global answer
    answer = max(answer, tmp)

def go(cnt, idx):
    if idx == n:
        calc()
        return 

    for i in range(idx, n):
        # 뽑거나
        subset.append(p[i])
        go(cnt + 1, i + 1)
        subset.pop()
        
        # 안뽑거나
        go(cnt, i + 1)

go(0, 0)
print(answer)