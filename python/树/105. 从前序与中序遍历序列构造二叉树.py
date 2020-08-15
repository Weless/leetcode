class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        rootVal = preorder[0]
        i = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder[1:i+1],inorder[:i])
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root

# 优化
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        dic = {v:i for i,v in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(left,right):
            if left > right:
                return
            val = preorder[self.pre_idx]
            self.pre_idx +=1
            root = TreeNode(val)
            index = dic[val]
            root.left = dfs(left,index-1)
            root.right = dfs(index+1,right)
            return root
        return dfs(0,len(inorder)-1)