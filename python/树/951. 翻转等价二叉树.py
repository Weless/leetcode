class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1.val != root2.val:
            return False
        if root1.left.val != root2.left.val or root1.right.val != root2.right.val:
            root1.left,root1.right = root1.right,root1.left
        left = self.flipEquiv(root1.left,root2.left)
        right = self.flipEquiv(root2.right,root2.right)
        return left and right
