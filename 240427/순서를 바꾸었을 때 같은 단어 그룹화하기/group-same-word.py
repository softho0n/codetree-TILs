import sys

n = int(input())
d = {}

for _ in range(n):
    s = list(sys.stdin.readline().rstrip())
    s.sort()
    s = ''.join(s)

    if not s in d:
        d[s] = 1
    else:
        d[s] += 1

answer = -1
for k, v in d.items():
    if answer <= v:
        answer = v
print(answer)