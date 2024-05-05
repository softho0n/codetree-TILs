import sys


n = int(input())
a = list(map(int, sys.stdin.readline().split()))

answer = 1000000000


def calc(idx):
    tmp_sum = 0
    tmp_list = []

    for i in range(n):
        if i == idx:
            continue
        
        tmp_list.append(a[i])
    
    for i in range(1, len(tmp_list)):
        tmp_val = abs(tmp_list[i] - tmp_list[i-1])
        tmp_sum += tmp_val
    
    return tmp_sum


for i in range(n):
    a[i] = a[i] * 2
    for j in range(n):
        if i == j:
            continue
        
        answer = min(answer, calc(j))

    a[i] = a[i] // 2


print(answer)