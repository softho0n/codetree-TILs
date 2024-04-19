import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 0
for i in range(n):
    tmp_sum = arr[i] + arr[2*n - i -1]
    answer = max(answer, tmp_sum)

print(answer)