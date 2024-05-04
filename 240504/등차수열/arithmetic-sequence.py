import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
min_a = min(a)
max_a = max(a)

answer = 0

def verify(i, k, j):
    test_case = [a[i], k, a[j]]
    if a[i] - k == k - a[j]:
        return True
    return False

for k in range(min_a, max_a + 1):

    tmp_cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if verify(i, k, j):
                tmp_cnt += 1
    
    answer = max(answer, tmp_cnt)

print(answer)