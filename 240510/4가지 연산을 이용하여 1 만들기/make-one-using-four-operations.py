import sys



from collections import deque
import heapq


n = int(input())
v = [False] * (1000000 + 1)
c = [0] * (1000000 + 1)
q = deque()
q.append(n)
v[n] = True

answer = 0
while q:
    cp = q.popleft()

    if cp - 1 >= 1:
        if v[cp - 1] is False:
            v[cp - 1] = True
            q.append(cp - 1)
            c[cp-1] = c[cp] + 1
    
    if cp + 1 <= 1000000:
        if v[cp + 1] is False:
            v[cp + 1] = True
            q.append(cp + 1)
            c[cp+1] = c[cp] + 1
    
    if cp % 2 == 0:
        if v[cp // 2] is False:
            v[cp // 2] = True
            q.append(cp // 2)
            c[cp // 2] = c[cp] + 1
    
    if cp % 3 == 0:
        if v[cp // 3] is False:
            v[cp // 3] = True
            q.append(cp // 3)
            c[cp // 3] = c[cp] + 1

print(c[1])