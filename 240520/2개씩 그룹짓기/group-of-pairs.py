import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

max_val = -1
while a:
    val1 = a.pop(0)
    val2 = a.pop()
    val3 = val1 + val2

    if max_val < val3:
        max_val = val3
print(max_val)