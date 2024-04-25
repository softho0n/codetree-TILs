import sys

a = list(input())
answer = 0

for i in range(len(a)-1):
    if a[i] == '(' and a[i+1] == '(':
        for j in range(i+1, len(a)-1):
            if a[j] == ')' and a[j+1] == ')':
                answer += 1

print(answer)