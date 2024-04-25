import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = -1
for i in range(n):
    for j in range(i+2, n):
        answer = max(answer, a[i] + a[j])
print(answer)