import sys

x, y = map(int, sys.stdin.readline().split())

answer = 0

for i in range(x, y+1):

    t = f"{x}"
    t = list(t)
    tmp = 0

    for item in t:
        tmp += int(item)
    
    answer = max(answer, tmp)

print(answer)