import sys

n = int(input())
dol = [0, 0, 0]
cmd = []

for _ in range(n):
    cmd.append(
        list(map(int, sys.stdin.readline().split()))
    )

answer = 0
for i in range(3):
    testcase = [0, 0, 0]
    testcase[i] = 1
    ptn = 0
    for a, b, c in cmd:
        a_bak = testcase[a-1]
        b_bak = testcase[b-1]

        testcase[a-1] = b_bak
        testcase[b-1] = a_bak

        if testcase[c-1] == 1:
            ptn += 1
    
    answer = max(answer, ptn)

print(answer)