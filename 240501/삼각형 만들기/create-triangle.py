import sys



n = int(input())
ptns = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptns.append((x, y))

answer = 0

def calc(s):
    global answer
    if s[0][0] == s[1][0] and s[1][0] != s[2][0]:
        if s[1][1] != s[2][1]:
            tmp = abs(s[1][0] - s[2][0]) * abs(s[0][1]-s[1][1])
            answer = max(answer, tmp)
            return
    
    if s[0][0] == s[2][0] and s[2][0] != s[1][0]:
        if s[2][1] != s[1][1]:
            tmp = abs(s[2][0] - s[1][0]) * abs(s[0][1]-s[2][1])
            answer = max(answer, tmp)
            return

    if s[1][0] == s[2][0] and s[2][0] != s[0][0]:
        if s[2][1] != s[0][1]:
            tmp = abs(s[2][0]-s[0][0]) * abs(s[1][1] - s[2][1])
            answer = max(answer, tmp)
            return

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sample = [ptns[i], ptns[j], ptns[k]]
            calc(sample)

print(answer)