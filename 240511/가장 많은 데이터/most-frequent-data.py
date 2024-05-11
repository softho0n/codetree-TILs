import sys
from collections import defaultdict
n = int(input())
d = defaultdict(int)

for _ in range(n):
    s = input()
    d[s] += 1

answer = -1
for k,v in d.items():
    answer = max(answer, v)

print(answer)