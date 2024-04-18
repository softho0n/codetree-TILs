import sys





n, t = map(int, sys.stdin.readline().split())

#       N (2)
#       |
# L (0) - R (3)
#       |
#       S (1) 

dy = [0, 1, -1, 0]
dx = [-1, 0, 0, 1]
dir_dict = {}
dir_dict['L'] = 0
dir_dict['R'] = 3
dir_dict['N'] = 2
dir_dict['S'] = 1

r, c, d = sys.stdin.readline().split()
cur_d = dir_dict[d]

r = int(r) - 1
c = int(c) - 1

current_time = 0
while current_time < t:
    ny, nx = r + dy[cur_d], c + dx[cur_d]

    if ny < 0 or nx < 0 or ny >= n or nx >= n:
        cur_d = 3 - cur_d
        ny = ny + dy[cur_d]
        nx = nx + dx[cur_d]

        r = ny
        c = nx
        current_time += 1
        continue
    
    r = ny
    c = nx
    current_time += 1

print(r + 1, c + 1)