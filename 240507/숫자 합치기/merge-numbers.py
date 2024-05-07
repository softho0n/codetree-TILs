import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

answer = 0



while True:
    if len(a) == 1:
        break
    
    a1, a2 = a[0], a[1]
    a3 = a1 + a2
    answer += a3

    a.pop(0)
    a.pop(0)
    a.append(a3)

print(answer)