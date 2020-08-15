class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 1. 先序遍历树 A 中的每个节点nA （对应函数 isSubStructure(A, B)）
# 2. 判断树 A中 以 nA为根节点的子树 是否包含树 B。（对应函数 recur(A, B)）

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A,B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left,B.left) and recur(A.right,B.right)
        if not A or not B:
            return False
        return recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)