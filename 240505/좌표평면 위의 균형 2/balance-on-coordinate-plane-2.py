import sys


n = int(input())
ptns = []

max_v = -1
min_v = 101

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ptns.append((x, y))

    tmp_min = min(x, y)
    tmp_max = max(x, y)

    max_v = max(max_v, tmp_max)
    min_v = min(min_v, tmp_min)

if min_v % 2 != 0:
    min_v += 1

if max_v % 2 != 0:
    max_v += 1

subset = []
answer = 200
def calc1():
    # x, y
    a1, a2, a3, a4 = 0, 0, 0, 0
    for x, y in ptns:
        if x < subset[0] and y < subset[1]:
            a1 += 1
        elif x < subset[0] and y > subset[1]:
            a2 += 1
        elif x > subset[0] and y > subset[1]:
            a3 += 1
        elif x > subset[0] and y < subset[1]:
            a4 += 1

    max_a = max(a1, a2, a3, a4)
    global answer
    answer = min(answer, max_a)

def calc2():
    # x, y
    a1, a2, a3, a4 = 0, 0, 0, 0
    for x, y in ptns:
        if x < subset[1] and y < subset[0]:
            a1 += 1
        elif x < subset[1] and y > subset[0]:
            a2 += 1
        elif x > subset[1] and y > subset[0]:
            a3 += 1
        elif x > subset[1] and y < subset[0]:
            a4 += 1
    
    max_a = max(a1, a2, a3, a4)
    global answer
    answer = min(answer, max_a)

def go(cnt):
    if cnt == 2:
        calc1()
        calc2()
        return
    else:
        for i in range(min_v, max_v+1, 2):
            subset.append(i)
            go(cnt + 1)
            subset.pop()

go(0)
print(answer)