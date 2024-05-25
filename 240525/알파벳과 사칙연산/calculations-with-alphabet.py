import sys
from collections import defaultdict
s = list(sys.stdin.readline().rstrip())
alpha = [
    item
    for item in s
    if item.isalpha()
]

alpha = list(set(alpha))

answer = -10000000000
k = []
def calc():
    d = defaultdict(str)
    for a, v in k:
        d[a] = v
    tmp = 0

    # print(s, d)

    stack = []
    tmp = d[s[0]]
    for i in range(0, len(s)):
        if s[i] in '-*+':
            val1 = tmp
            val2 = d[s[i+1]]
            val3 = 0

            if s[i] == '-':
                val3 = val1 - val2
            elif s[i] == '+':
                val3 = val1 + val2
            elif s[i] == '*':
                val3 = val1 * val2

            # print(val3)
            tmp = val3
    return tmp

def go(cnt, idx):
    if cnt == len(alpha):
        # print(s)
        aaa = calc()
        global answer
        answer = max(answer, aaa)
        return
    else:
        for i in range(idx, len(alpha)):
            for j in range(1, 5):
                k.append((alpha[i], j))
                go(cnt + 1, i + 1)
                k.pop()
go(0, 0)
print(answer)