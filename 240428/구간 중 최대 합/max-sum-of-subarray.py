import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
s = -1

for i in range(n-k+1):
    b = 0
    for p in range(k):
        b += a[i+p]
    s = max(s, b)
print(s)