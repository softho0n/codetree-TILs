import sys
n = int(input())
a = [''] * (101)

for _ in range(n):
    p, c = sys.stdin.readline().split()
    p = int(p)
    a[p] = c

answer = 0
for i in range(101):
    for j in range(i, 101):
        subset = a[i:j+1]

        g_cnt = 0
        h_cnt = 0
        idx = []
        for q, item in enumerate(subset):
            if item == 'G':
                g_cnt += 1
                idx.append(q)  
            elif item == 'H':
                h_cnt += 1
                idx.append(q)
            
        if g_cnt == h_cnt and h_cnt > 0:
            answer = max(answer, idx[-1] - idx[0])
        elif g_cnt == 0 and h_cnt > 0:
            answer = max(answer, idx[-1] - idx[0])
        elif g_cnt > 0 and h_cnt == 0:
            answer = max(answer, idx[-1] - idx[0])
        
print(answer)