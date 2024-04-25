import sys
s = list(input())

answer = 0
for i in range(len(s)):
    if s[i] == '(':
        for j in range(i+1, len(s)):
            if s[j] == ')':
                answer += 1

print(answer)