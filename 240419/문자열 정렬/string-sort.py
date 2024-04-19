import sys

s = list(sys.stdin.readline().rstrip())
s.sort()

answer = "".join(s)
print(answer)