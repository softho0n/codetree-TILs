import sys
n, h, t = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

answer = 100000000
for i in range(n-t+1):
    cost = 0
    for j in range(t):
        cost += abs(h - a[j+i])
    answer = min(answer, cost)
print(answer)