import sys

a = list(input())
a = [int(item) for item in a]
c = []
for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
        joint = ''.join([f"{item}" for item in a])
        c.append(int(joint, 2))
        a[i] = 0
    else:
        a[i] = 0
        joint = ''.join([f"{item}" for item in a])
        c.append(int(joint, 2))
        a[i] = 1
c.sort()
print(c[-1])