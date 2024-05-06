import sys

n, m = map(int, sys.stdin.readline().split())
info = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    info.append((w, v, v / w))

info.sort(key=lambda x: x[2], reverse=True)
s = 0

tmp_sum = 0
for w, v, _ in info:
    if m == 0:
        break

    if m - w >= 0:
        m = m - w
        tmp_sum += v
    else:
        tmp_sum += v * (m / w)
        m = m - w * (m / w)

print(f'{tmp_sum:.3f}')