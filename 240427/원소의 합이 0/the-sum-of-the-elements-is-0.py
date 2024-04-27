import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            for p in range(n):
                s = a[i] + b[j] + c[k] + d[p]
                if s == 0:
                    answer += 1
print(answer)