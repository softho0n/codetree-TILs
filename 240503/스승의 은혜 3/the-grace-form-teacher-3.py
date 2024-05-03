N, B = map(int, input().split())
gifts_info = [list(map(int, input().split())) for _ in range(N)]

max_students = 0
for i in range(N):
    gifts_info[i][0] //= 2
    prices = [(gifts_info[j][0] + gifts_info[j][1]) for j in range(N)]
    # 값이 바뀌면 안 됨
    gifts_info[i][0] *= 2
    prices.sort()

    students, cur_prices = 0, 0

    for j in range(N):
        if cur_prices + prices[j] > B:
            break

        cur_prices += prices[j]
        students += 1

    max_students = max(max_students, students)

print(max_students)