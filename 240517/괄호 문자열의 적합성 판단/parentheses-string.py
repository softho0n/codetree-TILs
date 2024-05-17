import sys
s = list(input())
a = []

for i in range(len(s)):
    if s[i] == "(":
        a.append("(")
    else:
        if len(a) == 0:
            print("No")
            exit(0)
        a.pop()

if len(a) >= 1:
    print("No")
else:
    print("Yes")