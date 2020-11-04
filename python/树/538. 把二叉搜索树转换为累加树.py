class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 思路：
# 二叉搜索树的性质：
# 1. 中序遍历递增有序
# 2. 根节点的大于左子树的值，小于右子树的值
# 题目要找到某个节点，所有大于等于该节点的值
# 中序遍历的逆序和即满足条件
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.sum += root.val
            root.val = self.sum
            dfs(root.left)

        dfs(root)
        return root