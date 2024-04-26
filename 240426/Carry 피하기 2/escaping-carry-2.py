import sys
n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

v = [False] * n
answer = 0
s = []

def verify():
    s1, s2, s3 = s[0], s[1], s[2]
    while s1 > 0 or s2 > 0 or s3 > 0:
        a1 = s1 % 10
        a2 = s2 % 10
        a3 = s3 % 10
        if a1 + a2 + a3 >= 10:
            return False
        
        s1 = s1 // 10
        s2 = s2 // 10
        s3 = s3 // 10
    
    return True

        

def go(cnt, idx):
    if cnt == 3:
        if verify():
            global answer
            answer = max(answer, sum(s))
        return
    else:
        for i in range(idx, n):
            if v[i] is False:
                v[i] = True
                s.append(a[i])
                go(cnt + 1, i + 1)
                s.pop()
                v[i] = False

go(0, 0)
if answer == 0:
    print(-1)
else:
    print(answer)