import sys
from collections import defaultdict

s = list(sys.stdin.readline().rstrip())
d = defaultdict(int)
for item in s:
    d[item] += 1

candidate = []
for k, v in d.items():
    if v == 1:
        candidate.append(k)
    
if len(candidate) == 0:
    print("None")
else:
    for item in s:
        if d[item] == 1:
            print(item)
            exit(0)