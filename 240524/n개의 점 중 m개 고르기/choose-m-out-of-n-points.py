import math
import sys

n, m = map(int, sys.stdin.readline().split())
ptns = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptns.append((x, y))

s = []
answer = 1000000000000
def get_distance(i, j):
    xi, yi = s[i]
    xj, yj = s[j]
    tmp = (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj)
    return tmp

def calc():
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            distance = get_distance(i, j)
            global answer
            answer = min(answer, distance)

def go(cnt, idx):
    if cnt == m:
        calc()
        return
    else:
        for i in range(idx, n):
            s.append(ptns[i])
            go(cnt + 1, i + 1)
            s.pop()

go(0, 0)
print(answer)