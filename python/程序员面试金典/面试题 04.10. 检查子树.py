class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def seri(root):
            if not root: return "#"
            left = seri(root.left)
            right = seri(root.right)
            return left + ',' + str(root.val) + ',' + right

        self.t2_seri = seri(t2)
        def dfs(root):
            if not root: return False
            if seri(root) == self.t2_seri:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            return left or right
        return dfs(t1)


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return not t2
        if t2 == None:
            return True
        # find the root of t2 in t1
        return self.dfs(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def dfs(self, t1, t2):
        # t2 is over
        if t2 == None:
            return True
        # t2 is not over and t1 is over
        elif t2 != None and t1 == None:
            return False
        # not equal
        elif t2.val != t1.val:
            return False
        # equal, then search left and right
        else:
            return self.dfs(t1.left, t2.left) and self.dfs(t1.right, t2.right)  # 注意这里是and
