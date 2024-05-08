import sys
import heapq
from bisect import bisect_right

n = int(sys.stdin.readline().rstrip())
total_number = {i for i in range(1,(2*n)+1)}

b_nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
total_number = list(total_number - set(b_nums))

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