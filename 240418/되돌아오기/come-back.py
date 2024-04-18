import sys





n = int(input())
# 남, 북, 동, 서
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
dir_dict = {}

dir_dict['W'] = 3
dir_dict['S'] = 0
dir_dict['N'] = 1
dir_dict['E'] = 2

answer = 0
y, x = 0, 0
for _ in range(n):
    d, k = sys.stdin.readline().split()
    cur_d = dir_dict[d]
    k = int(k)

    for _ in range(k):
        ny = y + dy[cur_d]
        nx = x + dx[cur_d]
        answer += 1

        if ny == 0 and nx == 0:
            print(answer)
            exit(0)
        
        y = ny
        x = nx
        # if ny < 0 or nx < 0 or ny >= n and nx >= n:
        #     print(-1)
        #     print("here")
        #     exit(0)

print(-1)