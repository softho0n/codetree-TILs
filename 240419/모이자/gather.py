import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

answer = sys.maxsize

for i in range(n):
    target = arr[i]
    tmp_sum = 0

    for j in range(n):
        tmp_sum += abs(j - i) * arr[j]
    
    answer = min(answer, tmp_sum)

print(answer)