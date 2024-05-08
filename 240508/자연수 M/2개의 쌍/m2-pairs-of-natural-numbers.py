import sys
import heapq

n = int(sys.stdin.readline().rstrip())
s = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    s.append((y, x))

s.sort()
li = 0
ri = n - 1

ans = 0
while li <= ri:
    ly, lx = s[li]
    ry, rx = s[ri]

    ans = max(ans, ly + ry)

    if lx == rx:
        li += 1
        ri -= 1
    elif lx < rx:
        # 왼쪽 갯수가 더 작다면
        s[ri] = (ry, rx - lx) 
        li += 1
    elif lx > rx:
        s[li] = (ly, lx - rx)
        ri -= 1

print(ans)