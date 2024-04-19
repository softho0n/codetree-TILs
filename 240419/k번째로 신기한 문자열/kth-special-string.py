import sys

n, k, t = sys.stdin.readline().split()
n = int(n)
k = int(k)

subset = []
for i in range(n):
    s = input()
    if s.startswith(t):
        subset.append(list(s))

subset.sort()
answer = subset[k-1]
answer = "".join(answer)
print(answer)