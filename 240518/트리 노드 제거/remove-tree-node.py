import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
parents = [0 for _ in range(n)]
childs = [
    []
    for _ in range(n)
]

for idx, item in enumerate(a):
    parents[idx] = item
    
    if item != -1:
        childs[item].append(idx)

d = int(input())
answer = 0

def go(s):
    # parent_s = parents[s]
    # if s in childs[parent_s]:
    #     childs[parent_s].remove(s)
    parents[s] = -2
    for next_pos in childs[s]:
        go(next_pos)

parent_s = parents[d]
if d in childs[parent_s]:
    childs[parent_s].remove(d)
    
go(d)
for i in range(n):
    if len(childs[i]) == 0 and parents[i] != -2:
        answer += 1

print(answer)