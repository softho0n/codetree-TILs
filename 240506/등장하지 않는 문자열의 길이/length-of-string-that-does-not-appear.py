import sys

a = int(input())
n = input()
na = list(n)

answer = 10000000000
def test(s):
    tmp = ""
    cnt = 0
    slen = len(s)
    for i in range(a):
        kk = na[i:i+slen]
        kk = "".join(kk)
        if kk == s:
            cnt += 1

    if cnt == 1:
        global answer
        answer = min(answer, len(s))


def test(s, step):
    cnt = 0
    for i in range(a):
        t = na[i:i+step]
        t = "".join(t)

        if t == s:
            cnt += 1
    
    if cnt >= 2:
        return True
    else:
        return False
        

for i in range(1, a+1):

    flag = True
    for j in range(a):
        test_str = "".join(na[j:j+i])
        if len(test_str) != i:
            continue
        
        if test(test_str, i):
            flag = False
            break

    if flag:
        print(i)
        exit()