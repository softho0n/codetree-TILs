import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
new_arr = sorted(arr)

# print(new_arr)
visited = [False] * (n + 1)

for item in arr:

    for i in range(n):
        target = new_arr[i]

        if item == target and visited[i] is False:
            print(i + 1, end=' ')
            visited[i] = True
            break