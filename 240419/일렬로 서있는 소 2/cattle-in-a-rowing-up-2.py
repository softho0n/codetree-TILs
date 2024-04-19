import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] <= a[j] and a[j] <= a[k]:
                answer += 1

print(answer)