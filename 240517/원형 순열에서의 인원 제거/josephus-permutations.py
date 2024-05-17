import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
a = deque([item for item in range(1, n + 1)])

while len(a) != 1:
    cnt = 0
    while True:
        if cnt == k-1:
            v = a.popleft()
            print(v, end=' ')
            break
        val = a.popleft()
        a.append(val)
        cnt += 1
print(a[0])