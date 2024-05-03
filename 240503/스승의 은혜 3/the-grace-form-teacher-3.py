import sys
n, b = map(int, sys.stdin.readline().split())
g = []
answer = 0
for _ in range(n):
    p, s = map(int, sys.stdin.readline().split())
    g.append([p, s])

for i in range(n):
    g[i][0] = g[i][0] // 2 
    price = [
        g[j][0] + g[j][1]
        for j in range(n)
    ]
    g[i][0] *= 2
    price.sort()
    
    tmp = 0
    cnt = 0
    for j in range(n):
        if tmp + price[j] <= b:
            tmp += price[j]
            cnt += 1
        else:
            break
    answer = max(answer, cnt)

print(answer)