from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root1)
        dfs(root2)
        return sorted(res)

# 中序遍历+归并排序
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, v):
            if not node:
                return
            dfs(node.left, v)
            v.append(node.val)
            dfs(node.right, v)

        v1, v2 = list(), list()
        dfs(root1, v1)
        dfs(root2, v2)
        ans, i, j = list(), 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                ans.append(v1[i])
                i += 1
            else:
                ans.append(v2[j])
                j += 1
        return ans
