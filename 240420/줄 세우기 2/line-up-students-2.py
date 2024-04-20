import sys
n = int(input())
sample = []

for i in range(n):
    h, w = sys.stdin.readline().split()
    h = int(h)
    w = int(w)
    sample.append((h, w, i + 1))

sample.sort(key=lambda x: (x[0], -x[1]))
for h, w, num in sample:
    print(f"{h} {w} {num}")