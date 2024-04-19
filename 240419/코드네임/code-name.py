import sys



sample = []
for _ in range(5):
    codename, score = sys.stdin.readline().split()
    sample.append((int(score), codename))
sample.sort()
print(f"{sample[0][1]} {sample[0][0]}")