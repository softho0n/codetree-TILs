import sys
from bisect import bisect_left, bisect_right

n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())

    lk = bisect_left(p, s)
    rk = bisect_right(p, e)

    # if lk < n and rk < n:
    #     print(s, e, lk, rk, p[lk], p[rk])
    print(rk-lk)