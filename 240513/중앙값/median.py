import heapq
import sys

t = int(input())
for _ in range(t):
    n = int(input())
    q = []

    a = list(map(int, sys.stdin.readline().split()))
    sorted_array = []
    for i in range(n):
        # heapq.heappush(q, a[i])

        if i % 2 != 0:
            continue
        else:
            q = a[:i+1]
            heapq.heapify(q)
            tmp = []
            for k in range(i // 2):
                v = heapq.heappop(q)
                tmp.append(v)
            print(q[0], end=' ')


    print()