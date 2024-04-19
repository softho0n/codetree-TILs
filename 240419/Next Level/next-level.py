import sys



class Sample:
    def __init__(self, _id, level):
        self._id = _id
        self.level = level
sample1 = Sample("codetree", 10)
cmd = sys.stdin.readline().split()
sample2 = Sample(cmd[0], int(cmd[1]))

print(f"user {sample1._id} lv {sample1.level}")
print(f"user {sample2._id} lv {sample2.level}")