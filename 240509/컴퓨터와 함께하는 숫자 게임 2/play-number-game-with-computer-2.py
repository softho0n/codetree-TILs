import sys

m = int(input())
a, b = map(int, sys.stdin.readline().split())
s = 1
e = m

def play(p):
    cnt = 0
    l = 1
    r = m

    while l <= r:
        mid = (l + r) // 2

        if p == mid:
            cnt += 1
            return cnt
        elif p < mid:
            r = mid - 1
            cnt += 1
        else:
            l = mid + 1
            cnt += 1

min_answer = 1000000000000
max_answer = -1

for i in range(a, b + 1):
    cnt = play(i)
    if cnt < min_answer:
        min_answer = cnt
    
    if cnt > max_answer:
        max_answer = cnt
    
print(min_answer, max_answer)