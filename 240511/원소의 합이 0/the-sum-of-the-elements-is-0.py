import sys
from collections import defaultdict
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

D = defaultdict(int)
for i in range(n):
    for j in range(n):
        tmp = c[i] + d[j]
        D[tmp] += 1

answer = 0
for i in range(n):
    for j in range(n):
        tmp = a[i] + b[j]
        tmp2 = 0 - (tmp)

        if tmp2 in D:
            answer += D[tmp2]

print(answer)