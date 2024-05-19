import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
parents = [0] * (1000001)
childs = [
    []
    for _ in range(1000001)
]
visited = [False for _ in range(1000001)]

root = a[0]
visited[root] = True
parents[root] = -1

tmp_list = []
i = 1

def find_new_parent():
    idx = 1000002
    for i in range(n):
        if visited[a[i]] is True and len(childs[a[i]]) == 0:
            idx = min(idx, a[i])
    return idx

def add_childs(p, c):
    for item in c:
        childs[p].append(item)
        parents[item] = p
        visited[item] = True
    
def get_parent(p):
    return parents[p]

while i < n:
    tmp_list = [a[i]]
    j = i + 1
    while j < n:
        if a[j] == a[i] + 1:
            tmp_list.append(a[j])
            j += 1
            i += 1
        else:
            break
    i += 1
    p = find_new_parent()
    add_childs(p, tmp_list)


kp = get_parent(k)
kkp = get_parent(kp)
if kkp == -1:
    print(0)

kkp_childs = childs[kkp]
kkp_childs = [item for item in kkp_childs if item != kp]
answer = 0
for item in kkp_childs:
    answer += len(childs[item])
print(answer)