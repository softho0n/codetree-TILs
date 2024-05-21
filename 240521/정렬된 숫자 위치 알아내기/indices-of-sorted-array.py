import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(a)
visited = [False for _ in range(n)]

for item in a:
    for i in range(n):
        if visited[i] is False and b[i] == item:
            print(i+1, end=' ')
            visited[i] = True
            break