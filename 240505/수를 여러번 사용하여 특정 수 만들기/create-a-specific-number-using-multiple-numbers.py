import sys



a, b, c = map(int, sys.stdin.readline().split())

A = c // a
B = c // b

answer = 0

for i in range(A+1):
    for j in range(B+1):
        tmp_sum = i * a + j * b
        if tmp_sum <= c:
            answer = max(answer, tmp_sum)
    

print(answer)