import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
def start(s):
    cnt = 0
    tmp_sum = 0
    while cnt != m:
        tmp_sum += a[s-1]
        s = a[s-1]
        cnt += 1
    return tmp_sum

for i in range(n):
    test = start(i)
    answer = max(answer, test)

print(answer)