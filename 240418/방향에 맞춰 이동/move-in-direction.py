import sys








n = int(input())
y, x = 0, 0

for _ in range(n):
    dir, k = sys.stdin.readline().split()
    k = int(k)
    if dir == 'N':
        y += k
    elif dir == 'E':
        x += k
    elif dir == 'S':
        y -= k
    elif dir == 'W':
        x -= k

print(x, y)