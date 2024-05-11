import heapq
import sys
n = int(input())
q = []

for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if len(cmd) == 1:
        if cmd[0] == "size":
            # print(q)
            print(len(q))
        elif cmd[0] == "pop":
            v = heapq.heappop(q)
            print(-v)
        elif cmd[0] == "empty":
            if len(q) == 0:
                print("1")
            else:
                print("0")
        elif cmd[0] == "top":
            print(-q[0])
    else:
        c = cmd[0]
        v = int(cmd[1])

        heapq.heappush(q, -v)
        # print(q)