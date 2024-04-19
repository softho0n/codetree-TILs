import sys

answer = 0
s = list(sys.stdin.readline().rstrip())
n = len(s)

for i in range(n):
    if s[i] == '(':
        for j in range(i+1, n):
            if s[j] == ')':
                answer += 1
    else:
        continue
print(answer)