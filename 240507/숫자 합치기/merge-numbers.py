import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

answer = 0

while True:
    tmp = []
    for i in range(0, len(a), 2):
        if i == len(a) - 1:
            tmp.append(a[i])
        else:
            tmp.append(a[i] + a[i+1])
            answer += a[i] + a[i+1]
    
    if len(tmp) == 1:
        break
    
    a.clear()
    for item in tmp:
        a.append(item)
    a.sort()

print(answer)