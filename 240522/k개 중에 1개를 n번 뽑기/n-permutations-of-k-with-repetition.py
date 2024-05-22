import sys
k, n = map(int, sys.stdin.readline().split())
a = [item for item in range(1, k+1)]

subset = []
def go(cnt):
    if cnt == n:
        print(*subset)
        return
    else:
        for i in range(1, k+1):
            subset.append(i)
            go(cnt+1)
            subset.pop()

go(0)