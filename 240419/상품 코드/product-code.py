import sys

class Box:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name, code = sys.stdin.readline().split()
code = int(code)
sample = Box("codetree", 50)
box = Box(name, code)

print(f"product {sample.code} is {sample.name}")
print(f"product {box.code} is {box.name}")