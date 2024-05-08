import sys

n = int(input())
info = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

info.sort(key=lambda x: (x[1], -x[0]))

answer = 0
second = 1

# print(info)

while True:
    if len(info) == 0:
        break
    
    v, s = info[0]
    if second <= s:
        # print(v, s)
        answer += v
        info.pop(0)
        second += 1
    else:
        while True:
            nv, ns = info[0]
            # print(nv, ns)
            if len(info) == 0:
                break

            if second <= ns:
                answer += nv
                info.pop(0)
                break
            info.pop(0)
        second += 1

print(answer)