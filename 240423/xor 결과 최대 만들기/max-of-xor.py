import sys
from functools import reduce
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = -1
subset = []
visited = [False for _ in range(n)]

def calc():
    res = reduce(lambda x, y: x ^ y, subset)
    global answer
    answer = max(answer, res)

def go(cnt):
    if cnt == m:
        calc()
        return
    else:
        for i in range(n):
            if visited[i] is False:
                visited[i] = True
                subset.append(arr[i])
                go(cnt + 1)
                subset.pop()
                visited[i] = False

go(0)
print(answer)