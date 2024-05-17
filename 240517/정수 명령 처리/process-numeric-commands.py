import sys


n = int(input())
a = []

for _ in range(n):
    c = list(sys.stdin.readline().split())
    if len(c) == 1:
        if c[0] == "size":
            print(len(a))
        elif c[0] == "empty":
            if len(a) == 0:
                print(1)
            else:
                print(0)
        elif c[0] == "pop":
            print(a[-1])
            del a[-1]
        elif c[0] == "top":
            print(a[-1])
    else:
        val = int(c[1])
        a.append(val)