import sys
from bisect import bisect_right

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
ts = set(total_number)
answer = 0

for b in b_nums:
    tb = b + 1

    if tb in ts:
        answer += 1
# for a, b in zip(total_number, b_nums):
#     if a > b:
#         answer += 1
# for b_num in b_nums:
#     r = bisect_right(total_number, b_num)

#     if r >= len(total_number):
#         continue
    
#     item = total_number[r]

#     total_number.pop(r)

#     if item > b_num:
#         answer += 1

print(answer)