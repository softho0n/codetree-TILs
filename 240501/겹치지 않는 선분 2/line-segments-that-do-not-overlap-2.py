import sys

n = int(input())
ptns = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptns.append((x, y))

answer = 0
for i in range(n):
    ix, iy = ptns[i]
    overlap = False
    for j in range(n):
        if i == j:
            continue
        
        cx, cy = ptns[j]
        
        if cx <= ix and iy <= cy:
            overlap = True
            continue
        
        if ix <= cx and cy <= iy:
            overlap = True
            continue
        
    
    if not overlap:
        answer += 1
        
print(answer)