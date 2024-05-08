import sys
import heapq
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

heapq.heapify(total_number)
heapq.heapify(b_nums)

test = heapq.heappop(b_nums)
answer = 0

while True:
    a_test = heapq.heappop(total_number)
    if a_test > test:
        answer += 1

        if len(total_number) > 0 and len(b_nums) > 0:
            test = heapq.heappop(b_nums)
        else:
            break

print(answer)