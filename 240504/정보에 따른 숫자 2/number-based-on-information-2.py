import sys
t, a, b = map(int, sys.stdin.readline().split())

info = [''] * (10001)
for _ in range(t):
    cmd = sys.stdin.readline().split()
    alpha = cmd[0]
    place = int(cmd[1])
    info[place] = alpha

answer = 0
def get_d1(x):
    d1 = 10000000000
    for i in range(1, x+1):
        if info[i] == 'S':
            distance = abs(x-i)
            d1 = min(d1, distance)
    
    for i in range(x+1, b+1):
        if info[i] == 'S':
            distance = abs(x-i)
            d1 = min(d1, distance)
    
    return d1

def get_d2(x):
    d2 = 10000000000
    for i in range(1, x+1):
        if info[i] == 'N':
            distance = abs(x-i)
            d2 = min(d2, distance)
    
    for i in range(x+1, b+1):
        if info[i] == 'N':
            distance = abs(x-i)
            d2 = min(d2, distance)
    
    return d2


for x in range(a, b + 1):
    d1 = get_d1(x)
    d2 = get_d2(x)

    if d1 <= d2:
        answer += 1

print(answer)