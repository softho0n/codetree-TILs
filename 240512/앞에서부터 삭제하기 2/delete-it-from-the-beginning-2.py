import sys
import heapq

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

for k in range(1, n-1):
    a_copy = a[k:]
    print(a_copy)