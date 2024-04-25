import sys

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

def calc(skip_ptn):
    sy, sx = points[0][0], points[0][0]

    distance = 0
    for i in range(1, n):
        if i == skip_ptn:
            continue
        else:
            y, x = points[i][0], points[i][1]
            distance += abs(y-sy) + abs(x-sx)
            sy = y
            sx = x
    return distance

answer = 21e8
for i in range(1, n-1):
    answer = min(answer, calc(i))

print(answer)