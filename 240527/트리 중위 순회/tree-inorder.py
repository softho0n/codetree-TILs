import sys



k = int(input())
tree = [0 for _ in range(2**k + 1)]

a = list(map(int, sys.stdin.readline().split()))

def buildTree(inorder, idx):
    if len(inorder) == 0:
        return
    
    mid = len(inorder) // 2

    tree[idx] = inorder[mid]
    buildTree(inorder[:mid], idx * 2)
    buildTree(inorder[mid+1:], idx * 2 + 1)

buildTree(a, 1)

for i in range(k):
    tmp = 2 ** i
    for j in range(tmp, tmp + tmp):
        print(tree[j], end=' ')
    print()
# for i in range(1, 2**k):
#     print(tree[i], end=' ')
#     if (i - 1) % 2 == 0:
#         print()