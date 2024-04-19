class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

import sys

code, color, sec = sys.stdin.readline().split()
sec = int(sec)
b = Bomb(code, color, sec)

print(f"code : {b.code}")
print(f"color : {b.color}")
print(f"second : {b.sec}")