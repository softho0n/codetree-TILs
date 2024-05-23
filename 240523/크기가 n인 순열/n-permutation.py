import sys

n = int(input())
subset = []
visited = [False for _ in range(n + 1)]
def go(cnt):
    if cnt == n:
        print(*subset)
        return
    else:
        for i in range(1, n+1):
            if visited[i]:
                continue
            
            visited[i] = True
            subset.append(i)
            go(cnt + 1)
            subset.pop()
            visited[i] = False

go(0)