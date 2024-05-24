import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

subset = []
answer = 0
def go(cnt, idx):
    if cnt == m:
        tmp = subset[0]
        for i in range(1, len(subset)):
            tmp = tmp ^ subset[i]
        global answer
        answer = max(answer, tmp)
        return
    else:
        for i in range(idx, n):
            subset.append(a[i])
            go(cnt + 1, i + 1)
            subset.pop()
    
go(0, 0)
print(answer)