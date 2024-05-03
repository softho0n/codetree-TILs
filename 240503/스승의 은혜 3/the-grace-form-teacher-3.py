import sys





n, b = map(int, sys.stdin.readline().split())
info = []
for _ in range(n):
    p, s = map(int, sys.stdin.readline().split())
    info.append((p, s))
answer = 0

def calc(i, j):
    total_sum = 0
    for step in range(i, j+1):
        total_sum += info[step][0]
        total_sum += info[step][1]
    return total_sum

answer = 0
for i in range(n):
    for j in range(i+1, n):
        original_sum = calc(i, j)
        # print(f"{i} {j} {original_sum}")
        for k in range(i, j+1):
            pivot = original_sum - info[k][0] // 2
            if pivot <= b:
                answer = max(answer, j-i+1)

print(answer+1)