import sys
n = int(input())
a = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    a.append((s, e))

a.sort(key=lambda x: x[1])
answer = 0

for i in range(n):
    cnt = 1
    cur_endtime = a[i][1]

    for j in range(i+1, n):
        js, je = a[j]
        if cur_endtime <= js:
            cnt += 1
            cur_endtime = je
        else:
            continue
    
    answer = max(answer, cnt)
print(answer)