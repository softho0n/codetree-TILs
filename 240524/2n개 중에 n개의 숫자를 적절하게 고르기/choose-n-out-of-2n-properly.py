import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
sum_a = sum(a)
subset = []

answer = 100000000
def go(cnt, idx):
    if cnt == n:
        a1 = [item for item in a if not item in subset]
        a1 = sum(a1)
        a2 = sum(subset)
        a3 = abs(a1 - a2)
        global answer
        answer = min(answer, a3)
        return
    else:
        for i in range(idx, 2*n):
            subset.append(a[i])
            go(cnt + 1, i + 1)
            subset.pop()

go(0, 0)
print(answer)