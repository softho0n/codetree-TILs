import sys






n, k = map(int, sys.stdin.readline().split())
b = []

for _ in range(n):
    b.append(int(input()))

answer = -1
for i in range(n-k+1):
    sample = b[i]
    tmp_answer = -1
    for j in range(1, k+1):
        if i + j >= n:
            continue
        if b[i+j] == sample:
            tmp_answer = sample
            break
    
    answer = max(answer, tmp_answer)
print(answer)