import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if i % 2 == 0:
        sample = sorted(arr[:i+1])
        print(sample[i // 2], end=' ')