import sys
n = int(input())


class Person:
    def __init__(self, name, addr, loc):
        self.name = name
        self.addr = addr
        self.loc = loc

sample = []
for _ in range(n):
    name, addr, loc = sys.stdin.readline().split()
    p = (name, addr, loc)
    sample.append(p)

sample.sort(reverse=True)
print(f"name {sample[0][0]}")
print(f"addr {sample[0][1]}")
print(f"city {sample[0][2]}")