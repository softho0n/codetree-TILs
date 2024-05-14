import sys
n = int(input())
energy = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

l = [0] * (n + 1)
l[0] = cost[0]

for i in range(1, n):
    l[i] = min(l[i-1], cost[i])

answer = 0
for i in range(n-1):
    answer += energy[i] * l[i]

print(answer)