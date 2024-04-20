import sys

k, n = map(int, sys.stdin.readline().split())

answer = []

def go(cnt):
    if cnt == n:
        print(*answer)
        return
    else:
        for i in range(1, k+1):
            answer.append(i)
            go(cnt + 1)
            answer.pop()

go(0)