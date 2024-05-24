import sys
n = int(input())
g = []

for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

visited = [False for _ in range(n+1)]
subset = []
answer = 100000000000
def go(cnt):
    if len(subset) == n:
        global answer

        tmp_visited = [False for _ in range(n+1)]
        tmp = 0
        flag = True
        for p, v in subset:
            if tmp_visited[p] is False:
                tmp_visited[p] = True
                tmp += v
            else:
                flag = False
                break
        
        if flag:
            answer = min(answer, tmp)
        # answer = min(answer, sum(subset))
        return
    else:
        for i in range(n):
            if visited[i]:
                continue
            if g[cnt][i] == 0:
                continue
            
            visited[i] = True
            subset.append((cnt, g[cnt][i]))
            go(i)
            subset.pop()
            visited[i] = False

go(0)
print(answer)