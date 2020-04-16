class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归，先序遍历（DFS）
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left,root.right = self.mirrorTree(root.right),self.mirrorTree(root.left)
        return root

# 辅助栈（队列）

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
