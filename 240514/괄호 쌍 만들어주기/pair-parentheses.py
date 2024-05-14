import sys

s = list(input())

ri = 0
li = 0
answer = 0
for i in range(len(s)-1):
    sub_str = "".join([s[i], s[i+1]])

    if sub_str == "((":
        ri += 1
    elif sub_str == "))":
        
        answer += ri

print(answer)