import sys



from collections import defaultdict


n = int(input())
# tree = {
#     "A": {
#         "left_child": "B",
#         "right_child": "C"
#     }
# }

tree = defaultdict(str)
for _ in range(n):
    A, B, C = sys.stdin.readline().split()
    tree[A] = {
        "left_child": B,
        "right_child": C
    }

def pa(root):
    if root == '.':
        return
    else:
        print(root, end='')
        pa(tree[root]["left_child"])
        pa(tree[root]["right_child"])

pa('A')
print()

def pb(root):
    if root == ".":
        return
    else:
        pb(tree[root]["left_child"])
        print(root, end='')
        pb(tree[root]["right_child"])

pb('A')
print()

def pc(root):
    if root == ".":
        return
    else:
        pc(tree[root]["left_child"])
        pc(tree[root]["right_child"])
        print(root, end='')
        

pc('A')
print()