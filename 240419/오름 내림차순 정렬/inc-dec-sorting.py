import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr1 = sorted(arr)
arr2 = sorted(arr, reverse=True)
print(*arr1)
print(*arr2)