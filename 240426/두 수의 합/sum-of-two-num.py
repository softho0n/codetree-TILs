import sys

d = {}
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for item in a:
    if not k - item in d:
        d[k-item] = 1
    else:
        d[k-item] += 1

answer = 0
for key, v in d.items():
    if k - key in d:
        sample = d[k - key]
        answer += sample * v
print(answer // 2)