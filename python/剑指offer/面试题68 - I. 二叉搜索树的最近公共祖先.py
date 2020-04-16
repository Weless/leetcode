# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val == q.val:
            return p
        while root:
            if root.val < q.val and root.val < p.val:
                root = root.right
            if root.val > q.val and root.val > p.val:
                root = root.left
            else:
                return root