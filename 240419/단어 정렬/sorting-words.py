import sys

n = int(input())
subset = []

for _ in range(n):
    subset.append(input())

subset.sort()
for item in subset:
    print(item)