import sys

n, q = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
arr = [0] * (1000000 + 1)

for item in p:
    arr[item] = 1

ps = [0] * (1000000 + 1)

for i in range(1, 1000000 + 1):
    ps[i] = ps[i-1] + arr[i]
    
# print(ps)
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    print(ps[b] - ps[a-1])