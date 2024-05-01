import sys

n, b = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    k = int(input())
    a.append(k)
a.sort()

answer = 0

for i in range(n):
    tmp = a[i] // 2
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        
        if tmp + a[j] <= b:
            tmp += a[j]
            cnt += 1
        else:
            break
    answer = max(answer, cnt)
print(answer)