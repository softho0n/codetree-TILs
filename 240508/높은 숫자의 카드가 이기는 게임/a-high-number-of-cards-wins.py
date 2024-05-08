import sys

n = int(input())
total_number = []

for i in range(1, 2*n + 1):
    total_number.append(i)

b_nums = []
for _ in range(n):
    b_num = int(input())
    b_nums.append(b_num)
    total_number.remove(b_num)

b_nums.sort()

answer = 0

for b_num in b_nums:

    test_num = b_num + 1

    for i in range(len(total_number)):
        if total_number[i] == test_num:
            answer += 1
            total_number.remove(test_num)
            break

print(answer)