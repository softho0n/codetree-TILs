import sys
n = int(input())

sample = []
for _ in range(n):
    date, day, _type = sys.stdin.readline().split()
    if _type != 'Rain':
        continue
    year, month, _day = date.split("-")
    concat_str = "".join([year, month, _day])
    sample.append((int(concat_str), day))

sample.sort()
answer_candidate = sample[0]
concat_str = f"{answer_candidate[0]}"
k = concat_str[:4] + "-" + concat_str[4:6] + "-" + concat_str[6:]
day = answer_candidate[1]

print(f"{k} {day} Rain")