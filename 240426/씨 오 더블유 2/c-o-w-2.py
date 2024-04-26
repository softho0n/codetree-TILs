import sys
n = int(input())
s = list(input())
answer = 0
v = [False] * n

subset = []
def go(cnt, idx):
    if cnt == 3:
        if subset[0] == 'C' and subset[1] == 'O' and subset[2] == 'W':
            print(subset)
            global answer
            answer += 1
        return
    else:
        for i in range(idx, n):
            if v[i] is False:
                v[i] = True
                subset.append(s[i])
                go(cnt + 1, i + 1)
                subset.pop()
                v[i] = False
go(0, 0)
print(answer)