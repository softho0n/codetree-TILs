import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()

for a_item, b_item in zip(a, b):
    if a_item != b_item:
        print("No")
        exit(0)
print("Yes")