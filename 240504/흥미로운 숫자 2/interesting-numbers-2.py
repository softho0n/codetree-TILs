import sys
from collections import defaultdict

x, y = map(int, sys.stdin.readline().split())
answer = 0

for i in range(x, y + 1):
    tmp = list(f"{i}")
    s = set()
    d = defaultdict(int)
    for item in tmp:
        s.add(item)
        d[item] += 1
    
    s = list(s)
    if len(s) == 2:
        for item in s:
            if d[item] == 1:
                answer += 1
print(answer)