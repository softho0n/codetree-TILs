import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in range(n):
    if i % 2 == 0:
        print(arr[i // 2], end=' ')