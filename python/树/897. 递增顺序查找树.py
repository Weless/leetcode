class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        inorder(root)
        start = cur = TreeNode(res[0])
        for i in res[1:]:
            cur.right = TreeNode(i)
            cur = cur.right
        return start