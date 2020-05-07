class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if s and not t:
            return True
        if not s and t:
            return False
        if s == t:
            left = self.isSubtree(s.left,t.left)
            right = self.isSubtree(s.right,t.right)
            return left and right
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)