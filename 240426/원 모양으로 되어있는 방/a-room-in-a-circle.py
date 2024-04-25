import sys
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))


answer = 1000000000000
for i in range(n):
    tmp_sum = 0

    for j in range(n):
        tmp_sum += ((j - i) % n) * a[j]
    
    answer = min(answer, tmp_sum)
print(answer)