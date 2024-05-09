import sys
from bisect import bisect_left, bisect_right

n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())

    rk = bisect_right(p, s)
    lk = bisect_left(p, e)

    print(lk - rk)