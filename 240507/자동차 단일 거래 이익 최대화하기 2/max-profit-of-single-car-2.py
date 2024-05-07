import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = -1

s, e = 0, 0

while s < n and e < n:
    tmp = a[e] - a[s]
    if tmp >= 0:
        answer = max(answer, tmp)
        e = e + 1
    else:
        s = s + 1

if answer <= 0:
    print(0)
else:
    print(answer)