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

for i in range(len(n)):
    test_str = "".join(na[:i+1])
    test(test_str)

print(answer)