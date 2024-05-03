import sys






n, k = map(int, sys.stdin.readline().split())
b = []

for _ in range(n):
    b.append(int(input()))

answer = -1
for i in range(n):
    sample = b[i]
    tmp_answer = -1
    for j in range(i+1, i+k+1):
        if j >= n:
            break
        if sample == b[j]:
            tmp_answer = sample
            break
    answer = max(answer, tmp_answer)
print(answer)