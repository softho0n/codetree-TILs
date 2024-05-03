import sys

x, y = map(int, sys.stdin.readline().split())
answer = 0

for i in range(x, y + 1):
    tmp = list(f"{i}")
    s = set()
    for item in tmp:
        s.add(item)
    
    s = list(s)
    if len(s) == 2:
        answer += 1
        print(tmp)

print(answer)