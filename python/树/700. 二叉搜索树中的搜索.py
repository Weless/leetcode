class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if val < root.val:
            return self.searchBST(root.left,val)
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right,val)

# 迭代
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == val:
                    return node
                stack.append(node.left)
                stack.append(node.right)
        return
