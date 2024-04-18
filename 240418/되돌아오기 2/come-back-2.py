import sys





cmd = list(sys.stdin.readline().rstrip())

# 오른쪽, 아래쪽, 왼쪽, 위쪽 -> 시계 방향
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

answer = 0

cur_d = 3
y, x = 0, 0
for item in cmd:
    if item == 'L':
        # 0이면 3로
        # 1이면 0로
        # 2이면 1로
        # 3이면 2로
        cur_d = (cur_d - 1) % 4
        answer += 1
    elif item == 'R':
        # 0이면 1로
        # 1이면 2로
        # 2이면 3로
        # 3이면 0으로
        cur_d = (cur_d + 1) % 4
        answer += 1
    elif item == 'F':
        ny = y + dy[cur_d]
        nx = x + dx[cur_d]
        answer += 1
        if ny == 0 and nx == 0:
            print(answer)
            exit(0)
        y = ny
        x = nx

print(-1)