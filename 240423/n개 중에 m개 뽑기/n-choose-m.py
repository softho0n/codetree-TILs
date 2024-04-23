import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False for _ in range(n+1)]
subset = []

def print_subset():
    for item in subset:
        print(item, end=' ')
    print()

def go(cnt, idx):
    if cnt == m:
        print_subset()
        return
    else:
        for i in range(idx, n+1):
            subset.append(i)
            go(cnt + 1, i + 1)
            subset.pop()

go(0, 1)