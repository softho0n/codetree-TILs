from functools import cmp_to_key

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

# custom comparator를 직접 정의
# x가 앞에 있는 숫자, y가 뒤에 있는 숫자 가정했을 때
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을, 
# 반대라면 0보다 큰 값을
# 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# 보통 반환값에 1, -1, 0을 사용합니다.
def compare(x, y):
    # x가 y보다 크다면
    # 우리가 원하는 방향입니다.
    sx = int(list(f"{x}")[0])
    sy = int(list(f"{y}")[0])

    if sx > sy:
        return -1
    if sy > sx:
        return 1
    if sy == sx:
        xy = int(f"{x}{y}")
        yx = int(f"{y}{x}")

        if xy > yx:
            return -1
        elif xy < yx:
            return 1
        else:
            return 0

a.sort(key=cmp_to_key(compare))

for elem in a: # 정렬 이후의 결과 출력
    print(elem, end="")