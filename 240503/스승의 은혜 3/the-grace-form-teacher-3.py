import sys





n, b = map(int, sys.stdin.readline().split())
info = []
for _ in range(n):
    p, s = map(int, sys.stdin.readline().split())
    info.append((p, s))
answer = 0
info.sort()
for i in range(n):

    tmp = info[i][0] // 2 + info[i][1]
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        else:
            if tmp + info[j][0] + info[j][1] <= b:
                tmp += info[j][0]
                tmp += info[j][1]
                cnt += 1
            else:
                break
    answer = max(answer, cnt)
print(answer)