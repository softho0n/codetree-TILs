import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a = set(a)

m = int(input())
b = list(map(int, sys.stdin.readline().split()))
bs = set(b)

for item in b:
    if item in a:
        print(1, end=' ')
    else:
        print(0, end=' ')