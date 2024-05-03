import sys
n = int(input())
ptn = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptn.append((x, y))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            c = [0] * 101
            flag = True
            for p in range(n):
                if p == i or p == j or p == k:
                    continue
                
                x, y = ptn[p]
                for item in range(x, y+1):
                    c[item] += 1
            
            for item in c:
                if item >= 2:
                    flag = False
                    break
            
            if flag:
                answer += 1

print(answer)