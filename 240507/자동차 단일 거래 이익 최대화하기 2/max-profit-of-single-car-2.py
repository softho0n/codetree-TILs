import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = -1

for i in range(n):
    sample = a[i]
    for j in range(i+1, n):
        if sample < a[j]:
            answer = max(answer, a[j] - sample)

if answer == -1:
    print(0)
else:
    print(answer)