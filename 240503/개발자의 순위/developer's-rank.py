import sys






k, n = map(int, sys.stdin.readline().split())
m = []
for _ in range(k):
    m.append(
        list(map(int, sys.stdin.readline().split()))
    )

answer = 0

def verify(i, j):
    flag = True
    for r in m:
        A = r.index(i)
        B = r.index(j)

        if A > B:
            return False

    return flag

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        
        if verify(i, j):
            answer += 1

print(answer)