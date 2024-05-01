import sys



n = int(input())
t = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append((a, b))

answer = 0
for i in range(n):
    marking = [0] * (1001)
    for j in range(n):
        if i == j:
            continue
        
        a, b = t[j]
        for k in range(a, b):
            marking[k] += 1
    
    total_sum = 0
    for k in range(1001):
        if marking[k] >= 1:
            total_sum += 1
    
    answer = max(answer, total_sum)

print(answer)