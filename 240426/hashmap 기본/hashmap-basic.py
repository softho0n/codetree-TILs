import sys

n = int(input())
d = {}
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    c = cmd[0]

    if c == 'add':
        k = int(cmd[1])
        v = int(cmd[2])
        d[k] = v
    elif c == 'find':
        k = int(cmd[1])
        if not k in d:
            print("None")
        else:
            print(d[k])
    else:
        k = int(cmd[1])
        d.pop(k)