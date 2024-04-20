import sys

n = int(input())
sample = []
answer = 0

def is_answer():
    pivot = sample[0]
    cnt = 1

    for i in range(1, len(sample)):
        if pivot != sample[i]:
            if cnt % pivot != 0:
                return False
            else:
                pivot = sample[i]
                cnt = 1
        else:
            cnt += 1
    
    if cnt % pivot != 0:
        return False
    
    return True

def go(cnt):
    if cnt == n:
        if is_answer():
            global answer
            answer += 1
        return
    else:
        for i in range(1, 5):
            sample.append(i)
            go(cnt + 1)
            sample.pop()

go(0)
print(answer)