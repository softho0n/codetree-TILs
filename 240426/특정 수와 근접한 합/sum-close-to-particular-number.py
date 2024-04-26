import sys
n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answer = 100000000000

def calc(A, b):
    tmp_sum = 0
    for i in range(n):
        if i == A or i == b:
            continue
        tmp_sum += a[i]
    
    global answer
    answer = min(answer, abs(s - tmp_sum))
for i in range(n):
    for j in range(i+1, n):
        calc(i, j)

print(answer)