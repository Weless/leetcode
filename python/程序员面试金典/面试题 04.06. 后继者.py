class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root or not p: return
        if root.val <= p.val:
            return self.inorderSuccessor(root.right,p)
        else:
            left = self.inorderSuccessor(root.left,p)
            return left if left else root