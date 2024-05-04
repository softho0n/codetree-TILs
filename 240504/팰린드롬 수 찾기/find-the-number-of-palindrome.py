import sys

x, y = map(int, sys.stdin.readline().split())
cnt = 0

for test in range(x, y + 1):
    tmp = f"{test}"

    flag = True
    for i in range(len(tmp) // 2):
        if tmp[i] != tmp[len(tmp) - 1 - i]:
            flag = False
            break
    
    if flag:
        cnt += 1

print(cnt)