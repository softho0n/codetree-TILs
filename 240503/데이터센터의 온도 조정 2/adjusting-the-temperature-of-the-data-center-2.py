import sys
n, c, g, h = map(int, sys.stdin.readline().split())
temp = []

min_temp = 10000
max_temp = -1

for _ in range(n):
    ta, tb = map(int, sys.stdin.readline().split())
    temp.append((ta, tb))

    if min_temp > ta:
        min_temp = ta
    
    if max_temp < tb:
        max_temp = tb


def get_point(l, m, r):
    if m < l:
        return c
    elif l <= m and m <= r:
        return g
    elif m > r:
        return h

answer = 0
for test in range(min_temp-1, max_temp + 1):
    tmp_sum = 0
    for t1, t2 in temp:
        tmp_sum += get_point(t1, test, t2)
    answer = max(answer, tmp_sum)
print(answer)