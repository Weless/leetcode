class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def check(a:TreeNode,b:TreeNode):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val == b.val:
                return check(a.left,b.left) and check(a.right,b.right)
            return False
        if not s:
            return False
        return check(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)