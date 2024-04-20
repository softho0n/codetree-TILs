import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
answer = 0

for _ in range(n):
    graph.append(
        list(map(int, sys.stdin.readline().split()))
    )

def check_row(tmp_list):
    pivot = tmp_list[0]
    cnt = 1

    if m == 1:
        return True
    
    max_v = -1
    for i in range(1, len(tmp_list)):
        if pivot == tmp_list[i]:
            cnt += 1
        else:
            max_v = max(max_v, cnt)
            cnt = 1
            pivot = tmp_list[i]

    max_v = max(max_v, cnt)
    if max_v >= m:
        return True
    return False

for i in range(n):
    if check_row(graph[i]):
        answer += 1

for j in range(n):
    col = []
    for i in range(n):
        col.append(graph[i][j])
    if check_row(col):
        answer += 1

print(answer)