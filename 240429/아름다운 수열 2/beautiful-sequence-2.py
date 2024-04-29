import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
b.sort()

answer = 0
for i in range(n-m+1):
    subset = []
    for k in range(m):
        subset.append(a[i+k])
    subset.sort()
    if subset == b:
        answer += 1

print(answer)