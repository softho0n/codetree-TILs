import sys
n = int(input())
d = {}
for _ in range(n):
    s = input()
    if not s in d:
        d[s] = 1
    else:
        d[s] += 1

a = []
for k, v in d.items():
    a.append(v)
a.sort()
print(a[-1])