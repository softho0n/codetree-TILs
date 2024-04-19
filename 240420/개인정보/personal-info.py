import sys
sample = []

for _ in range(5):
    name, h, w = sys.stdin.readline().split()
    h = int(h)
    w = float(w)

    sample.append((name, h, w))

sample.sort(key=lambda x: x[0])
print("name")
for name, h, w in sample:
    print(f"{name} {h} {w}")

sample.sort(key=lambda x:x[1], reverse=True)
print()
print("height")
for name, h, w in sample:
    print(f"{name} {h} {w}")