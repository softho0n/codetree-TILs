import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()
set_a = set(a)
set_b = set(b)
a = list(set_a)
b = list(set_b)

for i in range(n):
    if a[i] != b[i]:
        print("No")
        exit(0)
print("Yes")