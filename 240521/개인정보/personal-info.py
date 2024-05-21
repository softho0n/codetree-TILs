import sys
a = []

for _ in range(5):
    name, h, w = sys.stdin.readline().split()
    h = int(h)
    w = float(w)
    a.append((name, h, w))

a.sort()
print("name")
for n, h, w in a:
    print(n, h, w)

print()
a.sort(key=lambda x:-x[1])
print("height")
for n, h, w in a:
    print(n, h, w)