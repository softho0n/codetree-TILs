import sys
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

min_a = min(a)
max_a = max(a)
answer = 0

for x in range(min_a, max_a + 1):
    tmp_sum = 0


    flag = False
    for i in range(n):
        if a[i] > x:
            flag = True
        else:
            if flag:
                tmp_sum += 1
                flag = False
    
    if flag:
        tmp_sum += 1
    answer = max(answer, tmp_sum)
print(answer)