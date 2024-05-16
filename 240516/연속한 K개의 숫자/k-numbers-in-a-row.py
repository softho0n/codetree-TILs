import sys
n, k, b = map(int, sys.stdin.readline().split())
bl = []

for _ in range(b):
    bl.append(int(sys.stdin.readline().rstrip()))

total = [item for item in range(0, n+1)]
origin = []
for i in range(0, n+1):
    if i in bl:
        origin.append(0)
    else:
        origin.append(i)
borigin = []
for i in range(0, n+1):
    if i in bl:
        borigin.append(i)
    else:
        borigin.append(0)
ts = [0] * (n + 1)
os = [0] * (n + 1)
bs = [0] * (n + 1)
bcnt = [0] * (n + 1)
for i in range(1, n + 1):
    ts[i] = ts[i-1] + total[i]
for i in range(1, n + 1):
    os[i] = os[i-1] + origin[i]
for i in range(1, n + 1):
    bs[i] = bs[i-1] + borigin[i]
for i in range(1, n + 1):
    if borigin[i] != 0:
        bcnt[i] = bcnt[i-1] + 1
    else:
        bcnt[i] = bcnt[i-1]
# print(total)
# print(origin)
# print(borigin)

# print(ts)
# print(os)
# print(bs)
# print(bcnt)
answer = 10000000
for i in range(n+1):
    if i+k <= n:
        tmp1 = ts[i+k] - ts[i]
        tmp2 = os[i+k] - os[i]
        tmp3 = bs[i+k] - bs[i] 

        if tmp1 == tmp2 + tmp3:
            tmp_answer = 0
            tmp4 = bcnt[i+k] - bcnt[i]
            answer = min(answer, tmp4)
            # # for j in range(i+1, i+1+k):
            # #     if borigin[j] != 0:
            # #         tmp_answer += 1
            # # answer = min(answer, tmp_answer)
            # print(i, tmp1, tmp2, tmp3, tmp4)
print(answer)