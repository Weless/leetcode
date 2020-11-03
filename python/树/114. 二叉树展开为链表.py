class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 左子树变成链表
        self.flatten(root.left)
        # 右子树变成链表
        self.flatten(root.right)

        temp = root.right
        # 树的右边换成左边的链表
        root.right = root.left
        # 左边置空
        root.left = None
        # 找到树的最右边的节点
        while root.right: root = root.right
        # 把右边的链表接到刚才树的最右边的节点
        root.right = temp

# 后序遍历改，先遍历右子树再遍历左子树
class Solution:
    pre = None
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root
