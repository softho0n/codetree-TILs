import sys

n = int(input())
s = set()

for _ in range(n):
    c = list(sys.stdin.readline().split())
    cmd = c[0]
    if cmd == 'find':
        k = int(c[1])
        if k in s:
            print("true")
        else:
            print("false")
    elif cmd == 'add':
        k = int(c[1])
        s.add(k)
    elif cmd == 'remove': 
        k = int(c[1])
        s.remove(k)