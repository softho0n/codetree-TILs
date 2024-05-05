import sys

n = int(input())
ptns = []

min_val = 1000000
max_val = -1
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    min_tmp_k = min(x, y)
    max_tmp_k = max(x, y)

    if min_tmp_k < min_val:
        min_val = min_tmp_k
    
    if max_tmp_k > max_val:
        max_val = max_tmp_k

    ptns.append((x,y))

subset = []

def calc():
    # x, x, x

    tmp = 0
    for x, y in ptns:
        if x in subset:
            tmp += 1
    
    if tmp == len(ptns):
        print("c1")
        return True

    # x, x, y
    tmp = 0
    for x, y in ptns:
        if x == subset[0] or x == subset[1] or y == subset[2]:
            tmp += 1
    
    if tmp == len(ptns):
        print("c2")
        return True

    # x, y, x
    tmp = 0
    for x, y in ptns:
        if x == subset[0] or x == subset[2] or y == subset[1]:
            tmp += 1
    
    if tmp == len(ptns):
        print("c3")
        return True
        
    # x, y, y
    tmp = 0
    for x, y in ptns:
        if x == subset[0] or y == subset[1] or y == subset[2]:
            tmp += 1
    
    if tmp == len(ptns):
        print("c4")
        return True

    # y, x, x
    tmp = 0
    for x, y in ptns:
        if y == subset[0] or x == subset[1] or x == subset[2]:
            tmp += 1
    
    if tmp == len(ptns):
        print("c5")
        return True
        
    # y, x, y
    tmp = 0
    for x, y in ptns:
        if y == subset[0] or x == subset[1] or y == subset[2]:
            tmp += 1
    
    if tmp == len(ptns):
        print("c6")
        return True
        
    # y, y, x
    tmp = 0
    for x, y in ptns:
        if y == subset[0] or y == subset[1] or x == subset[2]:
            tmp += 1
    
    if tmp == len(ptns):
        print("c7")
        return True
        
    # y, y, y
    tmp = 0
    for x, y in ptns:
        if y in subset:
            tmp += 1
    
    if tmp == len(ptns):
        print("c8")
        return True
    
    return False
        
answer = 0
def go(cnt, next_val):
    if cnt == 3:
        if calc():
            print(*subset)
            global answer
            answer += 1
        return
    else:
        for i in range(next_val, max_val+1):
            subset.append(i)
            go(cnt + 1, i+1)
            subset.pop()

go(0, min_val)

if answer >= 1:
    print(1)
else:
    print(0)