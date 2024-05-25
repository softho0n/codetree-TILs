import sys

n, m = map(int, sys.stdin.readline().split())
ptns = []
position = [
    []
    for _ in range(n + 1)
]

max_h = -1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    max_h = max(max_h, b)
    ptns.append((a, b))
    position[a].append((1, b))
    position[a+1].append((-1, b))

for i in range(1, n+1):
    position[i].sort(key=lambda x: x[1])
first_state = []

for i in range(1, n+1):
    cx = i
    cy = 0

    while True:
        if cy == max_h:
            break

        changed = False
        for _dir, y_pos in position[cx]:
            if cy < y_pos:
                cy = y_pos
                cx = cx + _dir
                changed = True
                break
        
        if not changed:
            cy = max_h
    
    first_state.append(cx)
# print(first_state)
            

s = []
answer = 10000000
def play():
    position = [
        []
        for _ in range(n + 1)
    ]
    # print(s)

    for a, b in s:
        position[a].append((1, b))
        position[a+1].append((-1, b))

    for i in range(1, n+1):
        position[i].sort(key=lambda x: x[1])
    
    second_state = []

    for i in range(1, n+1):
        cx = i
        cy = 0

        while True:
            if cy == max_h:
                break

            changed = False
            for _dir, y_pos in position[cx]:
                if cy < y_pos:
                    cy = y_pos
                    cx = cx + _dir
                    changed = True
                    break
            
            if not changed:
                cy = max_h
        
        second_state.append(cx)
    
    # print(second_state)
    return second_state


def go(cnt, idx, target):
    if cnt == target:
        # print(s)
        sample = play()
        if sample == first_state:
            # print(sample, s)
            global answer
            answer = min(answer, len(s))
        return
    else:
        for i in range(idx, len(ptns)):
            s.append(ptns[i])
            go(cnt + 1, i + 1, target)
            s.pop()
        
for i in range(0, m+1):
    go(0, 0, i)

print(answer)