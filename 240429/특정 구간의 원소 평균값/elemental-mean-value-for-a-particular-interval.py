import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        k = j - i + 1
        s = sum(a[i:j+1])
        t = a[i:j+1]
        s = s // k

        if s in t:
            answer += 1

print(answer)