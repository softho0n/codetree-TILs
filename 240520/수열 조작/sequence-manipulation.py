import sys
from collections import deque

n = int(input())
a = deque([item for item in range(1, n + 1)])

while True:
    if len(a) == 1:
        break
    
    val = a.popleft()
    val2 = a.popleft()
    a.append(val2)

print(a[0])