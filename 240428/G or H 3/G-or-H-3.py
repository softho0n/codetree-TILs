import sys

n, k = map(int, sys.stdin.readline().split())
p = [0] * (20001)

a = []
for _ in range(n):
    c = list(sys.stdin.readline().split())
    x = int(c[0])
    y = c[1]

    if y == 'G':
        p[x] = 1
    else:
        p[x] = 2


answer = 0
for i in range(10000 - k + 2):
    b = 0

    for j in range(i, i+k+1):
        b += p[j]
    answer = max(answer, b)

print(answer)