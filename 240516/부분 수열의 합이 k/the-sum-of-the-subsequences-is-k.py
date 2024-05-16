import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.insert(0, 0)
ps = [0] * (n + 1)
ps[1] = a[1]
for i in range(2, n+1):
    ps[i] = ps[i-1] + a[i]

answer = 0
# for p in range(1, n):
#     for i in range(n):
#         if i + p >= n:
#             continue
#         tmp_sum = ps[i+p] - ps[i]
#         if tmp_sum == k:
#             answer += 1
#             print(i+p, i)

for i in range(n+1):
    for j in range(i+1, n+1):
        if ps[j] - ps[i] == k:
            answer += 1
print(answer)