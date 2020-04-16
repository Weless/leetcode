class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 二叉搜索树中序遍历为递增序列，则逆序的第k个节点，即为第k个节点
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        tmp = []
        def helper(root):
            if root.left:
                helper(root.left)
            tmp.append(root.val)
            if root.right:
                helper(root.right)

        helper(root)
        return tmp[-k]
