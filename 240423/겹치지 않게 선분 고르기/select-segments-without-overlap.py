import sys

n = int(input())
sample = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    sample.append((x, y))

subset = []
answer = 0

def overlap(i, j):
    ax1, ax2 = subset[i]
    bx1, bx2 = subset[j]

    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
            (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)

    

def solution():
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            if overlap(i, j):
                return False
    
    return True

def go(cnt):
    if cnt == n:
        if solution():
            global answer
            answer = max(answer, len(subset))
        return
    else:
        subset.append(sample[cnt])
        go(cnt + 1)
        subset.pop()

        go(cnt + 1)

go(0)
print(answer)