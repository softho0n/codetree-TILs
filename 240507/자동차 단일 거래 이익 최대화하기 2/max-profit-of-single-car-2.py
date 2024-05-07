import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = -1

s, e = 0, 0

while s < n and e < n:
    tmp = a[e] - a[s]
    # print(s, e)
    if tmp >= 0:
        answer = max(answer, tmp)
        e = e + 1
    else:
        s = s + 1
print(answer) 
# for i in range(n):
#     sample = a[i]
#     for j in range(i+1, n):
#         if sample < a[j]:
#             answer = max(answer, a[j] - sample)

if answer <= 0:
    print(0)
else:
    print(answer)