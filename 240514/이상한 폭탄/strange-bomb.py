import sys
n, k = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(int(input()))

l, r = 0, 1
tmp_l = 1
answer = -1

while l <= r and r < n:
    if tmp_l <= k and a[l] == a[r]:
        answer = max(answer, a[l])
        l += 1
        r = l + 1
        tmp_l = 1
    elif a[l] != a[r] and tmp_l < k:
        r = r + 1
        tmp_l += 1
    elif tmp_l == k and a[l] != a[r]:
        l += 1
        r = l + 1
        tmp_l = 1
print(answer)