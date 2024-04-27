import sys
from collections import defaultdict
n = int(input())
d = defaultdict(list)

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    d[x].append(y)

for k, v in d.items():
    v.sort()

answer = 0
for k, v in d.items():
    answer += v[0]

print(answer)