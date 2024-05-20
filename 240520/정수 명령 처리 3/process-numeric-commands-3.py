from collections import deque
import sys
n = int(input())
a = deque()

for _ in range(n):
    cmd = list(sys.stdin.readline().split())

    if len(cmd) == 2:
        if cmd[0] == "push_front":
            a.appendleft(int(cmd[1]))
        else:
            a.append(int(cmd[1]))
    else:
        if cmd[0] == "pop_front":
            print(a.popleft())
        elif cmd[0] == "pop_back":
            print(a.pop())
        elif cmd[0] == "size":
            print(len(a))
        elif cmd[0] == "empty":
            if a:
                print(0)
            else:
                print(1)
        elif cmd[0] == "front":
            print(a[0])
        elif cmd[0] == "back":
            print(a[-1])