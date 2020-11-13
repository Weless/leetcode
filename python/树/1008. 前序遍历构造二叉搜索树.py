from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        inorder = sorted(preorder)
        pre_value = preorder[0]
        node = TreeNode(pre_value)
        index = 0
        for i,v in enumerate(inorder):
            if v == pre_value:
                index = i
                break
        node.left = self.bstFromPreorder(preorder[1:index+1])
        node.right = self.bstFromPreorder(preorder[index+1:])
        return node