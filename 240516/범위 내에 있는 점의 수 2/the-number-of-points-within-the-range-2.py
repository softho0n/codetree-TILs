import sys

n, q = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
ps = [0] * (1000000 + 1)

for i in range(1, 1000000 + 1):
    if i in p:
        ps[i] = ps[i-1] + 1
    else:
        ps[i] = ps[i-1]

# print(ps)
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    print(ps[b] - ps[a-1])