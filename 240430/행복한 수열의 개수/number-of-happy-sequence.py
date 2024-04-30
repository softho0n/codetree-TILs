import sys

n,m = map(int, sys.stdin.readline().split())
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n):
    row = g[i]
    
    cnt = 1
    prev = row[0]
    flag = True
    for j in range(1, n):
        if prev == row[j]:
            cnt += 1
            if cnt >= m:
                flag = False
                answer += 1
                break
        else:
            if cnt >= m:
                flag = False
                answer += 1
                break
            cnt = 1
            prev = row[j]
    
    if flag and cnt >= m:
        answer += 1

for j in range(n):
    col = []
    for i in range(n):
        col.append(g[i][j])
    
    cnt = 1
    prev = col[0]
    flag = True

    for i in range(1, n):
        if prev == col[i]:
            cnt += 1
            if cnt >= m:
                flag = False
                answer += 1
                break
        else:
            if cnt >= m:
                flag = False
                answer += 1
                break
            cnt = 1
            prev = col[i]

    if flag and cnt >= m:
        answer += 1
        
print(answer)