import sys

n = int(input())
subset = []
answer = 0
def test(s):
    if len(s) == 1:
        if s[0] == 1:
            return True
        else:
            return False

    first_item = s[0]
    tmp_cnt = 1
    for i in range(1, len(s)):
        if first_item == s[i]:
            tmp_cnt += 1
        else:
            if tmp_cnt % first_item != 0:
                return False
            first_item = s[i]
            tmp_cnt = 1
    
    if tmp_cnt % first_item != 0:
        return False
    return True



def go(cnt):
    if cnt == n:
        if test(subset):
            global answer
            answer += 1
        return
    else:
        for i in range(1, 5):
            subset.append(i)
            go(cnt + 1)
            subset.pop()

go(0)
print(answer)