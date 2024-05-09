import sys
from bisect import bisect_left, bisect_right

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    k = int(input())
    lk = bisect_left(a, k)
    rk = bisect_right(a, k)
    print(rk - lk)