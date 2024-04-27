import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

dd = {}
for item in d:
    if not item in dd:
        dd[item] = 1
    else:
        dd[item] += 1

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            K = a[i] + b[j] + c[k]
            KK = -K
            if KK in dd:
                answer += dd[KK]

print(answer)