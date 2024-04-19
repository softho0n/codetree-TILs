import sys

n = int(input())
sample = []
for _ in range(n):
    name, h, w = sys.stdin.readline().split()
    h = int(h)
    w = int(w)
    sample.append((name, h, w))

sample.sort(key=lambda x: x[1])
for item in sample:
    print(f"{item[0]} {item[1]} {item[2]}")