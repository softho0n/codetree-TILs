import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

if len(a) != len(b):
    print("No")
else:

    a.sort()
    b.sort()

    for a_item, b_item in zip(a, b):
        if a_item != b_item:
            print("No")
            exit(0)
    print("Yes")