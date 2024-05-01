import sys



n = int(input())
ptns = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptns.append((x, y))

answer = 3000000
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = ptns[i]
        x2, y2 = ptns[j]
        distance = (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)
        answer = min(answer, distance)


print(answer)