import sys
s = list(input())
a = []

for i in range(len(s)):
    if s[i] == "(":
        a.append("(")
    else:
        a.pop()
if len(a) >= 1:
    print("No")
else:
    print("Yes")