import sys
n, k = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(int(input()))

r = [0] * (n + 1)
d = {}
for i in range(n-1, -1, -1):
    if not a[i] in d:
        r[i] = -1
    else:
        r[i] = d[a[i]]
    
    d[a[i]] = i

answer = -1
for i in range(n):
    if r[i] != -1 and abs(i - r[i]) <= k:
        answer = max(answer, a[i])
print(answer)