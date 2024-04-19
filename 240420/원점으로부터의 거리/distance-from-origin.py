import sys
n = int(input())
sample = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    distance = abs(x - 0) + abs(y - 0)
    sample.append((i+1, x, y, distance))

sample.sort(key=lambda x: x[3])
for item in sample:
    print(item[0])