import sys

d = {}
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for item in a:
    if not item in d:
        d[item] = 1
    else:
        d[item] += 1
        
answer = 0
for key in set(a):
    if key == k - key:
        answer += (d[key] * d[key] - 1)
    else:
        if k - key in d:
            answer += (d[key] * d[k - key])
print(answer // 2)